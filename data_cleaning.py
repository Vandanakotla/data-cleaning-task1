import pandas as pd

# Load the dataset
df = pd.read_csv("raw_data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values with "Unknown"
df = df.fillna("Unknown")

# Save the cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned successfully!")
