# API URL
API_URL = "https://api.open-meteo.com/v1/forecast"

# Weather API parameters
PARAMS = {
    "latitude": 11.25,
    "longitude": 75.77,
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "windspeed_10m",
        "precipitation"
    ],
    }

# File paths
RAW_DATA_PATH = r"data/raw/weather_raw.csv"

CLEAN_DATA_PATH = r"data/processed/weather_cleaned.csv"

PLOTS_PATH = r"data/processed/plots/"

REPORT_PATH = r"data/processed/weather_report.csv"

LOG_FILE = r"pipeline.log"