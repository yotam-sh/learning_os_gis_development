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


# # Instead of this:
# def prof_upper(prof):
#     return prof.upper()

# df['profession'] = df['profession'].apply(prof_upper)

# Use this:
df['profession'] = df['profession'].apply(lambda x: x.upper())

# print(df[['first', 'last', 'sex', 'profession']].applymap(len)) # applymap works on same-type fields only or it throws errors

# --> Use what learned in day 4 and day 5 on the stackoverflow csv:

os.chdir(r'C:\Users\yotam\Documents\Python\material\for_future_lessons\2019survey_copy')
file_list = os.listdir(os.getcwd())

assert "survey_results_public.csv" == file_list[2], "work csv not found"
work_csv = file_list[2]
wcsv_path = os.path.normpath("\\".join([os.getcwd(), work_csv])) # set work csv path

assert "survey_results_schema.csv" == file_list[3], "schema csv not found"
schema_csv = file_list[3]
scsv_path = os.path.normpath("\\".join([os.getcwd(), schema_csv])) # set schema file path

df = pd.read_csv(wcsv_path, index_col='Respondent')
schema_df = pd.read_csv(scsv_path, index_col='Column').sort_index() # Sort by index 'Column'

filt = (df["Country"] == "Israel") & (df['ConvertedComp'] > 0) & df['LanguageWorkedWith'].str.contains('Python', na=False)
