from operator import index
import os
import numpy as np
import pandas as pd
from datetime import datetime

##

def load_data():
    # Set workspace and get list of files
    os.chdir(r'C:\Users\yotam\Documents\Python\material\for_future_lessons\stack-overflow-developer-survey-2022')
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
    comp_times = ['Yearly', 'Weekly']
    multiplier = [12, 4]
    sign = ['/', '*']

    for n in range(2):
        comp_filt = (df['CompFreq'] == comp_times[n])
        df['CompTotal'].replace(to_replace=[comp_times[n], 'CompFreq'], value=[lambda x: f'{x}{sign[n]}{multiplier[n]}', 'Monthly'], inplace=True)

    # print(df[df['Country'] == 'Israel'].value_counts('CompFreq'))
    # Filter
    filt = (df['Country'] == 'Israel') & (df['CompTotal'] > 0)
    relevant_cols = ['Country', 'CompTotal', 'YearsCode', 'YearsCodePro', 'EdLevel', 'CompFreq']

    filter_df = df[filt][relevant_cols]

    print(filter_df.value_counts('CompFreq'))

    # return filter_df

## 

df = load_data()
df = work_with_data(df)