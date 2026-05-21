# main.py

from scripts.api_fetch import fetch_weather_data
from scripts.data_cleaning import clean_data
from scripts.eda import perform_eda
from scripts.report import generate_report


print("=" * 40)
print(" WEATHER DATA PIPELINE")
print("=" * 40)

# STEP 1 — API Extraction

print("\n[1/4] Fetching API data...")

fetch_weather_data()

print("✓ Raw data saved")

# STEP 2 — Data Cleaning

print("\n[2/4] Cleaning data...")

clean_data()

print("✓ Missing values handled")
print("✓ Duplicates removed")
print("✓ Cleaned data saved")

# STEP 3 — EDA

print("\n[3/4] Performing EDA...")

perform_eda()

print("✓ Plots generated successfully")

# STEP 4 — Report Generation

print("\n[4/4] Generating report...")

generate_report()

print("✓ Weather report created")

# FINAL MESSAGE

print("\n" + "=" * 40)
print(" PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 40)