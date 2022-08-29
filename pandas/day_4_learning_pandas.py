# Day 4

import os
import numpy as np
import pandas as pd

classmates = {
    'first_name': ['Yotam', 'Shaked', 'Idan', 'Maia'],
    'last_name': ['Shavit', 'Yefet', 'Ben-Atar', 'Abeles'],
    'age': [26, 28, 27, 23],
    'sex': ['Male', 'Male', 'Male', 'Female'],
    'profession': ['GIS Professional', 'GIS Analyst', 'GIS Analyst', 'Bartender']
}

# Create a dataframe from the dictionary
df = pd.DataFrame(classmates)

# Remap the field names
df.rename(columns={'first_name': 'first',
                   'last_name': 'last'}, inplace=True)

# Add condition
# filt = (df['sex'] == 'Male')

# Change profession to one classmate
df.loc[0, 'profession'] = 'GIS Developer'
print(df.loc[0, ['first', 'profession']])