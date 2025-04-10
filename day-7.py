import pandas as pd

df = pd.read_csv("messydata.csv")

#to count how many emails are empty
# emptyEmails = df['email'].isna().sum()
# print(emptyEmails)

#extract emails into a new column
df['email'] = df['email'].str.extract(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')

#save the cleaned data
df.to_csv("cleaned_emails.csv", index = False)
# print(df['email'])

#Memory Optimization
#Large datase can crash our program if not optimized so lets tell pandas to use less RAM by specifying data types:

print(df.dtypes)
# df.info()

