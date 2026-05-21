import pandas as pd


def clean_data():

    # Load raw dataset

    df = pd.read_csv(
        r"data/raw/weather_raw.csv"
    )

    # Convert time column to datetime format

    df['time'] = pd.to_datetime(df['time'])

    # Handle missing values

    df.dropna(inplace=True)

    # Standardize column names

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )

    # Remove duplicate records

    df.drop_duplicates(inplace=True)

    # Save cleaned dataset

    df.to_csv(
        r"data/processed/weather_cleaned.csv",
        index=False
    )

    return df