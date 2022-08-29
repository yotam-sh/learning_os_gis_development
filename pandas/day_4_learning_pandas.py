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
