# Day 4

from dataclasses import field
import os
import numpy as np
import pandas as pd

# Change working dir to path with required .csv
os.chdir(r'C:\Users\yotam\Documents\Python\material\for_future_lessons\2019survey_copy')
# Get file list
file_list = os.listdir(os.getcwd())

# Make sure our target work .csv is in the folder
assert "survey_results_public.csv" == file_list[2], "work csv not found"
work_csv = file_list[2]
wcsv_path = os.path.normpath("\\".join([os.getcwd(), work_csv])) # set work csv path

# Make sure schema .csv is also in the folder
assert "survey_results_schema.csv" == file_list[3], "schema csv not found"
schema_csv = file_list[3]
scsv_path = os.path.normpath("\\".join([os.getcwd(), schema_csv])) # set schema file path

# Read the .csv files
df = pd.read_csv(wcsv_path, index_col='Respondent')
schema_df = pd.read_csv(scsv_path, index_col='Column').sort_index() # Sort by index 'Column'

# Set filter with three different columns
filt = (df["Country"] == "Israel") & (df['ConvertedComp'] > 0) & df['LanguageWorkedWith'].str.contains('Python', na=False)

# print(df.loc[filt, ['Hobbyist', 'ConvertedComp', 'LanguageWorkedWith']])

# Make column names uppercase
df.columns = [x.upper() for x in df.columns]

field_names = [x.upper() for x in ['Hobbyist', 'ConvertedComp', 'LanguageWorkedWith']]
print(df.loc[filt, field_names])