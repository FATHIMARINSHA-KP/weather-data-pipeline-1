# scripts/report.py

import pandas as pd


def generate_report():

    # Load cleaned dataset

    df = pd.read_csv(
        r"data/processed/weather_cleaned.csv"
    )

    # Number of observations

    Number_of_Observations = len(df)

    # Date range covered

    date_range = (
        str(df['time'].min())
        + " to " +
        str(df['time'].max())
    )

    # Average temperature

    Avg_Temperature = df["temperature_2m"].mean()

    # Maximum temperature

    Max_Temperature = df["temperature_2m"].max()

    # Minimum temperature

    Min_Temperature = df["temperature_2m"].min()

    # Total precipitation

    Total_precipitation = df["precipitation"].sum()

    # Create report dataframe

    report_df = pd.DataFrame({

        'Number_of_Observations': [Number_of_Observations],

        'Date_Range_Covered': [date_range],

        'Average_Temperature': [Avg_Temperature],

        'Maximum_Temperature': [Max_Temperature],

        'Minimum_Temperature': [Min_Temperature],

        'Total_Precipitation': [Total_precipitation]

    })

    # Save report

    report_df.to_csv(
        r"data/processed/weather_report.csv",
        index=False
    )