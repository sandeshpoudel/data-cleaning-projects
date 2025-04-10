import pandas as pd
import numpy as np

# Generate dummy emails (some valid, some invalid)
def generate_email(i):
    if i % 10000 == 0:
        return ""  # missing email
    elif i % 15000 == 0:
        return "invalid-email"  # invalid format
    else:
        return f"user{i}@example.com"

emails = [generate_email(i) for i in range(1,300001)]

#Generating 3 Lakhs of dummy datas in excel to practice

data = pd.DataFrame(
    {
        'id' : np.arange(1,300001),
        'value':np.random.rand(300000),
        'gender':np.random.choice(['Male','M','m','Female','f','F'],300000),
        'category':np.random.choice(['A','B','C',None],300000),
        'date':pd.date_range('2020-01-01', periods=300000,freq='T'),
        'email' : emails

    }
)
data.to_csv("messy_data.csv", index = False)

# In this example we generated arond 3lakhs dummy data.