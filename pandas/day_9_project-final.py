from operator import index
import os
import numpy as np
import pandas as pd
from datetime import datetime

##

def load_data():
    # Set workspace and get list of files
    os.chdir(r'C:\Users\user\Desktop\stack-overflow-developer-survey-2022')
    workdir_files = os.listdir(os.getcwd())

    # Set work and schema csv names
    main_csv = 'survey_results_public.csv'

    # File paths
    main_csv_path = os.path.join(os.getcwd(), main_csv)

    try:
        # Load dataframes
        df = pd.read_csv(main_csv_path, index_col='ResponseId')
    except Exception as e:
        print(e)
    else:
        return df

def work_with_data(df):

    # Convert 'CompFreq' values to be Monthly and Yearly values
    comp_times = ['Yearly', 'Monthly', 'Weekly']
    multiplier = [1, 12, 48]
    sign = ['*', '*', '*']

    df['YearlySalary'] = ''
    for n in range(3):
        conv_filt = (df['CompTotal'] > 0) & (df['CompFreq'] == comp_times[n])
        df[conv_filt]['YearlySalary'] = df['YearlySalary'].replace(to_replace='', value=df[conv_filt]['CompTotal'] * multiplier[n])
        # print(df[conv_filt]['YearlySalary'].head())
    # print(df[df['Country'] == 'Israel'].value_counts('CompFreq'))
    # Filter
    filt = (df['Country'] == 'Israel') & (df['CompTotal'] > 0)
    relevant_cols = ['YearsCode', 'YearsCodePro', 'EdLevel', 'YearlySalary']

    filter_df = df[filt][relevant_cols]

    print(filter_df.head())

    # return filter_df

## 

df = load_data()
df = work_with_data(df)