import pandas as pd
import numpy as np
import os

print(os.getcwd())

os.chdir(r"E:\UCDcode")

netflix_data = pd.read_csv("E:\\UCDcode\\supermarket_sales - Sheet1.csv", encoding = "ISO-8859-1")

print(netflix_data.head(3))

print(netflix_data.shape)

missing_values_count = netflix_data.isnull().sum()
print(missing_values_count)


# print(netflix_data[netflix_data["Date"] >= "01/10/2019"])

# print(netflix_data[(netflix_data["Payment"]=="Cash") & (netflix_data["City"]=="Mandalay") ].head())

drop_duplicates= netflix_data.drop_duplicates()
print(netflix_data.shape,drop_duplicates.shape)

drop_duplicates= netflix_data.drop_duplicates(subset=['Payment'])
print(netflix_data.shape,drop_duplicates.shape)
print(drop_duplicates.to_string())

netflix_data['year'] = pd.DatetimeIndex(netflix_data['Date']).year
netflix_data['month'] = pd.DatetimeIndex(netflix_data['Date']).month

print(netflix_data.head(5))



