# app/utils.py
import pandas as pd
import plotly.express as px

def load_data(country: str):
    """
    Loads solar data for the selected country.
    You can replace the CSV file paths with your actual cleaned data files.
    """
    # Example file paths (adjust to your project structure)
    file_paths = {
        "Benin": "data/benin_solar_data.csv",
        "Sierra Leone": "data/sierra_leone_solar_data.csv",
        "Togo": "data/togo_solar_data.csv"
    }

    try:
        data = pd.read_csv(file_paths[country])
    except FileNotFoundError:
        # Fallback dummy data if CSVs aren’t available yet
        data = pd.DataFrame({
            "Date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
            "Solar_Irradiance": [100, 150, 180, 130, 170, 200, 210, 190, 160, 175],
            "Temperature": [25, 26, 27, 25, 28, 29, 30, 28, 27, 26]
        })
    return data


def plot_solar_trends(data: pd.DataFrame, variable: str):
    """
    Creates an interactive line chart for a chosen solar variable.
    """
    fig = px.line(
        data,
        x="Date",
        y=variable,
        title=f"{variable} Over Time",
        markers=True
    )
    fig.update_layout(xaxis_title="Date", yaxis_title=variable)
    return fig


def filter_by_date(data: pd.DataFrame, start_date, end_date):
    """
    Filters data by a date range selected by the user.
    """
    filtered = data[(data["Date"] >= start_date) & (data["Date"] <= end_date)]
    return filtered


