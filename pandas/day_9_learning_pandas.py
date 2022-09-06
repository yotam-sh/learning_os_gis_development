# Day 9

import os
import numpy as np
import pandas as pd
from datetime import datetime

##

def init_work():
    os.chdir(r'C:\Users\yotam\Documents\Python\material\for_future_lessons\2019survey_copy')
    file_list = os.listdir(os.getcwd())
    wcsv_name = 'survey_results_public.csv'
    scsv_name = 'survey_results_schema.csv'
    return file_list, wcsv_name, scsv_name

def df_creator(file_list, wcsv_name, scsv_name):
    for file in file_list:
        if file == wcsv_name:
            try:
                # Set parameters to create a DataFrame
                d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %I-%p')
                wcsv_path = os.path.join(os.getcwd(), wcsv_name)

                # Create a DataFrame
                df = pd.read_csv(wcsv_path, index_col='Respondent')
            except Exception as e:
                print(e)
        
        elif file == scsv_name:
            try:
                scsv_path = os.path.join(os.getcwd(), scsv_name)
                schema_df = pd.read_csv(scsv_path, index_col='Column').sort_index()
            except Exception as e:
                print(e)

    return df, schema_df

def data_editing(df):
    return
    
##

file_list, wcsv_name, scsv_name= init_work()
df, schema_df = df_creator(file_list, wcsv_name, scsv_name)
print(df)
