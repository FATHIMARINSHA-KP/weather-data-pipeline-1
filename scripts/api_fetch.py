# import required libraries

import requests
import pandas as pd


def fetch_weather_data():

    # send request to API

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 28.61,
        "longitude": 77.20,
        "hourly": "temperature_2m,relative_humidity_2m,windspeed_10m,precipitation"
    }

    response = requests.get(url, params=params)

    # parse JSON response

    data = response.json()

    hourly_data = data["hourly"]

    # extracting columns

    time = hourly_data["time"]

    temperature = hourly_data["temperature_2m"]

    relative_humidity = hourly_data["relative_humidity_2m"]

    windspeed = hourly_data["windspeed_10m"]

    precipitation = hourly_data["precipitation"]

    # Convert to DataFrame

    df = pd.DataFrame({
        "time": time,
        "temperature_2m": temperature,
        "relative_humidity_2m": relative_humidity,
        "windspeed_10m": windspeed,
        "precipitation": precipitation
    })

    # Save raw CSV

    df.to_csv(
        r"data/raw/weather_raw.csv",
        index=False
    )

    return df