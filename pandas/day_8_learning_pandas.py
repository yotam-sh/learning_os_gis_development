# Day 8

import os
import numpy as np
import pandas as pd

##

def init_work():
    os.chdir(r'C:\Users\yotam\Documents\Python\material\for_future_lessons')
    file_list = os.listdir(os.getcwd())
    work_csv_name = 'ETH_1h.csv'
    return file_list, work_csv_name

def df_creator(file_list, csv_name):
    for file in file_list:
        if file == csv_name:
            df = pd.read_csv(os.path.join(os.getcwd(), csv_name))
            return df

    

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
file_list, csv_name = init_work()
df = df_creator(file_list, csv_name)
# print(data_editing(df))
