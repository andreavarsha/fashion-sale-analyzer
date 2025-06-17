import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fashion Sale Analyzer", page_icon="👗")
st.title("👗 Fashion Sale Analyzer")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV with columns: Name, Category, Price, Season", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📦 Raw Uploaded Data")
    st.write(df)

    # Define discount rules
    discounts = {
        "top": 0.10,
        "bottom": 0.15,
        "outerwear": 0.25,
        "accessory": 0.05
    }

    # Apply discounts
    df["DiscountRate"] = df["Category"].map(discounts).fillna(0)
    df["DiscountedPrice"] = df["Price"] * (1 - df["DiscountRate"])

    # Season filter
    season_filter = st.selectbox("🔍 Filter by season", ["All"] + sorted(df["Season"].unique()))
    if season_filter != "All":
        df = df[df["Season"] == season_filter]

    # Display result
    st.subheader("✅ Discounted Items")
    st.dataframe(df[["Name", "Category", "Price", "DiscountRate", "DiscountedPrice"]])

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Discounted Data as CSV",
        data=csv,
        file_name="discounted_fashion.csv",
        mime="text/csv"
    )
