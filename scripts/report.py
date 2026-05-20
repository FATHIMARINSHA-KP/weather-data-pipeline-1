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