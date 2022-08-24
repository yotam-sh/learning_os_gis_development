# day 2

import pandas as pd

classmates = {
    'first_name': ['Yotam', 'Shaked', 'Idan', 'Maia'],
    'last_name': ['Shavit', 'Yefet', 'Ben-Atar', 'Abeles'],
    'age': [26, 28, 27, 23],
    'profession': ['GIS Professional', 'GIS Analyst', 'GIS Analyst', 'Bartender']
}

df = pd.DataFrame(classmates)
print(df)