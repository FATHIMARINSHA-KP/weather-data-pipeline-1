# Convert time column to datetime format

df['time'] = pd.to_datetime(df['time'])
df['time']


# Handle missing values appropriately

df.isnull().sum()


# no missing values available 

# Standardize column names

df.columns = df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

# Remove duplicate records

df.duplicated().sum()

df.drop_duplicates()