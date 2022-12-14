# Day 6

import os
import numpy as np
import pandas as pd

##

def init_work():
    os.chdir(r'C:\Users\yotam\Documents\Python\material\for_future_lessons\2019survey_copy')
    file_list = os.listdir(os.getcwd())
    return file_list

def df_creator(wcsv_path, scsv_path):
    df = pd.read_csv(wcsv_path, index_col='Respondent')
    schema_df = pd.read_csv(scsv_path, index_col='Column').sort_index() # Sort by index 'Column'
    return df, schema_df

def check_csv(file_list):
    assert "survey_results_public.csv" == file_list[2], "work csv not found"
    work_csv = file_list[2]
    wcsv_path = os.path.normpath("\\".join([os.getcwd(), work_csv])) # set work csv path

    assert "survey_results_schema.csv" == file_list[3], "schema csv not found"
    schema_csv = file_list[3]
    scsv_path = os.path.normpath("\\".join([os.getcwd(), schema_csv])) # set schema file path

    return df_creator(wcsv_path, scsv_path)

def data_editing(df):

    # Drop NaN rows
    global important_columns
    important_columns = ['Age', 'ConvertedComp', 'Country', 'YearsCode', 'YearsCodePro']
    df.dropna(axis='index', how='any', subset=important_columns, inplace=True)

    df['YearsCode'].replace(to_replace=['Less than 1 year', 'More than 50 years'], value=[0, 51], inplace=True)
    try:
        df['YearsCode'] = df['YearsCode'].astype(float)
    except TypeError:
        print(TypeError)
    
    return df[important_columns]
##

df, schema_df = check_csv(init_work())
print(data_editing(df))
