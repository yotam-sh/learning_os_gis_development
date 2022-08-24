# day 2

import os
import pandas as pd

classmates = {
    'first_name': ['Yotam', 'Shaked', 'Idan', 'Maia'],
    'last_name': ['Shavit', 'Yefet', 'Ben-Atar', 'Abeles'],
    'age': [26, 28, 27, 23],
    'sex': ['Male', 'Male', 'Male', 'Female'],
    'profession': ['GIS Professional', 'GIS Analyst', 'GIS Analyst', 'Bartender']
}

# Create a dataframe from the dictionary
# df = pd.DataFrame(classmates)

# Print selected columns
# print(df[['first_name', 'age']])

# Print selected rows - iloc
# print(df.iloc[[0, 1], 4])

### Working with a dataset

os.chdir(r'C:\Users\user\Desktop\PyForFun\geopandas\day_2_pandas')
file_list = os.listdir(os.getcwd())

assert "survey_results_public.csv" == file_list[2], "work csv not found"
work_csv = file_list[2]
wcsv_path = os.path.normpath("\\".join([os.getcwd(), work_csv]))

assert "survey_results_schema.csv" == file_list[3], "schema csv not found"
schema_csv = file_list[3]
scsv_path = os.path.normpath("\\".join([os.getcwd(), schema_csv]))

df = pd.read_csv(wcsv_path)
schema_df = pd.read_csv(scsv_path)

