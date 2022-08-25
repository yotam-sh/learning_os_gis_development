# Day 3

import numpy as np
import pandas as pd

classmates = {
    'first_name': ['Yotam', 'Shaked', 'Idan', 'Maya'],
    'last_name': ['Shavit', 'Yefet', 'Ben-Atar', 'Abeles'],
    'age': [26, 28, 27, 23],
    'sex': ['Male', 'Male', 'Male', 'Female'],
    'profession': ['GIS Professional', 'GIS Analyst', 'GIS Analyst', 'Bartender']
}

df = pd.DataFrame(classmates)
df.set_index(['first_name', 'last_name'], inplace=True)

print(df.loc['Yotam'])