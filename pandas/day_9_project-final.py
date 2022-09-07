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
    # Convert yearly USD salary to NIS
    nis_rate = 3.42
    df['YearlyCompNIS'] = [i * nis_rate for i in df.ConvertedCompYearly]

    # Replace EdLevel values with shorter values
    ed_levels = ["Bachelor’s degree (B.A., B.S., B.Eng., etc.)",
                 "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)",
                 "Associate degree (A.A., A.S., etc.)",
                 "Other doctoral degree (Ph.D., Ed.D., etc.)",
                 "Professional degree (JD, MD, etc.)"]
    
    df.loc[~df["EdLevel"].isin(ed_levels), "EdLevel"] = "Non-Academic"
    df['EdLevel'].replace(to_replace=[ed_levels[0], ed_levels[1], ed_levels[2], ed_levels[3], ed_levels[4]], 
                          value=["Bachelor's", "Master's", "Associate", "Doctoral", "Professional"], inplace=True)

    # Filter
    filt = (df['Country'] == 'Israel') & (df['ConvertedCompYearly'] > 0)
    relevant_cols = ['EdLevel', 'YearsCode', 'YearsCodePro', 'WorkExp', 'YearlyCompNIS', 'Age', 'Gender', 'Sexuality', 'Accessibility', 'MentalHealth']
    filter_df = df[filt][relevant_cols]

    return filter_df

## 

df = load_data()
df = work_with_data(df)
print(df.value_counts(['EdLevel']))