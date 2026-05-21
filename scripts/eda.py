# scripts/eda.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def perform_eda():

    # Load cleaned dataset

    df = pd.read_csv(
        r"data/processed/weather_cleaned.csv"
    )

    # Dataset shape

    print("\nDataset Shape:")
    print(df.shape)

    # Data types

    print("\nData Types:")
    print(df.dtypes)

    # Missing value summary

    print("\nMissing Value Summary:")
    print(df.isnull().sum())

    # Descriptive statistics

    print("\nDescriptive Statistics:")
    print(df.describe())

    # =====================================================
    # 1. Temperature Trend Over Time
    # =====================================================

    plt.figure(figsize=(10, 5))

    sns.lineplot(
        x='time',
        y='temperature_2m',
        data=df
    )

    plt.title("Temperature Trend Over Time")

    
    plt.savefig(
        r"data/processed/plots/temperature_trend.png"
    )

    plt.close()

    # =====================================================
    # 2. Temperature vs Humidity
    # =====================================================

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        x='temperature_2m',
        y='relative_humidity_2m',
        data=df
    )

    plt.title("Temperature vs Humidity")


    plt.savefig(
        r"data/processed/plots/temperature_vs_humidity.png"
    )

    plt.close()

    # =====================================================
    # 3. Wind Speed Distribution
    # =====================================================

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df['windspeed_10m'],
        bins=20,
        kde=True
    )

    plt.title("Wind Speed Distribution")

    
    plt.savefig(
        r"data/processed/plots/wind_speed_distribution.png"
    )

    plt.close()