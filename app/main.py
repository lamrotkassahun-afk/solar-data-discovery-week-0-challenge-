# app/main.py
import streamlit as st
from app.utils import load_data, filter_by_date, plot_solar_trends

# Set Streamlit page config
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# --- Sidebar ---
st.sidebar.title("🌍 Solar Data Dashboard")
st.sidebar.markdown("Use the filters below to customize your view:")

# Country selection
country = st.sidebar.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])

# Load data
data = load_data(country)

# Variable selection
variable = st.sidebar.selectbox("Select Variable", ["Solar_Irradiance", "Temperature"])

# Date range selection
min_date, max_date = data["Date"].min(), data["Date"].max()
start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Filter data
filtered_data = filter_by_date(data, start_date, end_date)

# --- Main Content ---
st.title("☀️ Solar Energy Insights Dashboard")
st.markdown(f"### Country: **{country}** | Variable: **{variable}**")

# Data Preview
with st.expander("🔍 View Data Table"):
    st.dataframe(filtered_data)

# Chart Display
fig = plot_solar_trends(filtered_data, variable)
st.plotly_chart(fig, use_container_width=True)

# Summary Statistics
st.subheader("📊 Summary Statistics")
st.write(filtered_data[variable].describe())



