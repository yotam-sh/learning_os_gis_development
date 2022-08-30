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
filt = (df['profession'].str.contains('GIS', na=False))

# Make first names lowercase
df['first'] = df['first'].str.lower()

# print(df[filt][['first', 'profession']])

def prof_upper(prof):
    return prof.upper()

df['profession'] = df['profession'].apply(prof_upper)

print(df)