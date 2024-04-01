import pandas as pd
import numpy as np

# 1. Loading

df = pd.read_csv('laptop_price.csv', encoding='1251')
print(df.sample(5))

# 2. First analysis

print(df.dtypes)

print(df.isna().sum())

print(df.info())

print(df.describe())

print(df.describe(include=["object"]))