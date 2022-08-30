# Day 5

import os
import numpy as np
import pandas as pd
from day_4_learning_pandas import classmates

# Create a dataframe from the dictionary
df = pd.DataFrame(classmates)

# Remap the field names
df.rename(columns={'first_name': 'first',
                   'last_name': 'last'}, inplace=True)

# Add condition
# filt = (df['sex'] == 'Male')

# Change profession to one classmate
# df.loc[0, 'profession'] = 'GIS Developer'
# print(df.loc[0, ['first', 'profession']])

# df.at[0, 'profession'] = 'GIS Professional'
# print(df.loc[0])

# Add condition
filt = (df['profession'].str.contains('GIS', na=False))

# Make first names lowercase
df['first'] = df['first'].str.lower()

print(df[filt][['first', 'profession']])

