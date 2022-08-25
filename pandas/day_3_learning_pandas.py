# Day 3

import os
import numpy as np
import pandas as pd

# Change working dir to path with required .csv
os.chdir(r'C:\Users\user\Desktop\PyForFun\geopandas\day_2_pandas')
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
schema_df = pd.read_csv(scsv_path, index_col='Column').sort_index()

print(schema_df)