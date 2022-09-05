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
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
    return df

##

file_list, csv_name = init_work()
df = df_creator(file_list, csv_name)
data_editing(df)
print(df['Date'])