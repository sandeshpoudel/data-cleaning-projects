import pandas as pd

#read dataset
df = pd.read_csv("messy_data.csv")

#Extract email.
df['email'] = df['email'].str.extract(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')

#clean gender column with 1. Trim spaces, 2. Lowercase and 3. Replace shortcuts
df['gender'] = df['gender'].str.strip().str.lower().replace({'m':'male', 'f':'female'})
# print(df['gender'].unique())

#export to csv
df.to_csv("cleanded.csv", index=False)