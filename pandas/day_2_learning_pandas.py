# day 2

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

# Print selected columns
print(df[['first_name', 'age']])

# Print selected rows - iloc
print(df.iloc[[0, 1], 4])

# 