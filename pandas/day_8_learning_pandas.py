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
            # Set lambda function for date-time conversion
            d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %I-%p')
            # Read csv with date-time conversion
            df = pd.read_csv(os.path.join(os.getcwd(), csv_name), parse_dates=['Date'], date_parser=d_parser)
            return df

def data_editing(df):
    # Another way of coverting to date-time
    # df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
    return df

##

file_list, csv_name = init_work()
df = df_creator(file_list, csv_name)
# data_editing(df)
print(df.loc[0, 'Date'].day_name())