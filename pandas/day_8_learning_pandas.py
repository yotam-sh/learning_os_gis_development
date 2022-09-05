# Day 8

import os
import numpy as np
import pandas as pd
from datetime import datetime

##

def init_work():
    os.chdir(r'C:\Users\yotam\Documents\Python\material\for_future_lessons')
    file_list = os.listdir(os.getcwd())
    work_csv_name = 'ETH_1h.csv'
    return file_list, work_csv_name

def df_creator(file_list, csv_name):
    for file in file_list:
        if file == csv_name:
            # Set parameters to create a DataFrame
            d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %I-%p')
            csv_path = os.path.join(os.getcwd(), csv_name)

            # Create a DataFrame
            df = pd.read_csv(csv_path, index_col='Date', parse_dates=['Date'], date_parser=d_parser)

            return df

# def data_editing(df):
    # Another way of coverting to date-time
    # df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
    # filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))

    # return df.loc[filt]

##

file_list, csv_name = init_work()
df = df_creator(file_list, csv_name)
# print(data_editing(df))
print(df)
