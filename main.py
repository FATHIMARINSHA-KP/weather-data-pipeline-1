# PART 1 — IMPORT LIBRARIES

import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# PART 2 — API EXTRACTION

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


# PART 3 — DATA CLEANING

df['time'] = pd.to_datetime(df['time'])


# check missing values

print(df.isnull().sum())


# standardize column names 

df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

print(df.columns)


# remove duplicate records

df.drop_duplicates(inplace=True)



#PART 4 — EDA / PLOTS

# data set shape 

df.shape

# data types

df.dtypes

# Missing value summary

df.isnull().sum()

# Descriptive statistics

df.describe()

# Temperature trend over time

plt.figure(figsize = (10,5))
sns.lineplot(x = 'time', y= 'temperature_2m', data = df)
plt.title("Temperature trend over time")
plt.show()

# Temperature vs Humidity

sns.scatterplot(x = "temperature_2m", y = "relative_humidity_2m", data =df)
plt.title("Temperature vs Humidity")
plt.show()
                
# Wind speed distribution

sns.histplot( df['windspeed_10m'] , bins= 20, kde = True)
plt.title('Wind speed distribution')
plt.show()

plt.savefig(r"C:\Users\A S S A U L T\Desktop\weather_api_assignment\data\processed\plots\temperature_trend.png")
plt.savefig(r"C:\Users\A S S A U L T\Desktop\weather_api_assignment\data\processed\plots\Temperature vs Humidity.png")
plt.savefig(r"C:\Users\A S S A U L T\Desktop\weather_api_assignment\data\processed\plots\Wind speed distribution.png")
plt.close()


# PART 5 — REPORT GENERATION

Number_of_Observations = len(df)

date_range = str(df['time'].min()) + " to " + str(df['time'].max())

Avg_Temperature = df["temperature_2m"].mean()

Max_Temperature = df["temperature_2m"].max()

Min_Temperature = df["temperature_2m"].min()

Total_precipitation = df["precipitation"].sum()


report_df = pd.DataFrame({
    'Number_of_Observations': [Number_of_Observations ],
    
    'Date_Range_Covered': [date_range],

    'Average_Temperature': [Avg_Temperature],
    
    'Maximum_Temperature': [Max_Temperature ],
    
    'Minimum_Temperature': [Min_Temperature],
    
    'Total_Precipitation': [Total_precipitation]
})

report_df.to_csv(
    r"C:\Users\A S S A U L T\Desktop\weather_api_assignment\data\processed\weather_report.csv",
    index=False)

