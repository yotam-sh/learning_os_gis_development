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

def csv_manip(dataframe):
    df = dataframe
    
    # Create group by country
    country_grp = df.groupby(['Country'])
    # Define filter and set the dataframe
    filt = (df['ConvertedComp'] > 0) & df['LanguageWorkedWith'].str.contains('Python', na=False)
    # Set df as Israel data group
    df = country_grp.get_group('Israel')
    df = df[filt][['Age', 'Country', 'Hobbyist', 'ConvertedComp', 'YearsCodePro', 'Sexuality', 'LanguageWorkedWith', 'SocialMedia']]

    # Rename columns
    df.rename(columns={'ConvertedComp': 'SalaryUSD', 'LanguageWorkedWith': 'CodeLanguages'}, inplace=True)

    # Remap Hobbyist column values to bool
    df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})

    # Add a new row
    df = df.append({'Country': 'Israel',
                'Hobbyist': 'True',
                'SalaryUSD': 64000,
                'CodeLanguages': 'Python'},
                ignore_index=True)
    
    # Drop columns based on new defined filter
    # drop_filt = (df['Hobbyist'] == False)
    # df.drop(index=df[drop_filt].index, inplace=True)

    # Sort the dataframe
    df.sort_values(by='SalaryUSD', ascending=False, inplace=True)

    return df

def new_manip(df):
    # Apply filter
    filt = (df['ConvertedComp'] > 0) # & df['LanguageWorkedWith'].str.contains('Python', na=False)
    df = df[filt]

    # Create group
    country_group = df.groupby('Country')
    
    # Get mean and median salaries in Israel
    # print(country_group['ConvertedComp'].agg(['mean', 'median']).loc['Israel'])

    # Get sum of people who said they worked with Python in Israel
    # print(df.loc[df['Country'] == 'Israel']['LanguageWorkedWith'].str.contains('Python', na=False).sum())

    # Get % of people who said they worked with Python in each country
    know_python = country_group['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python', na=False).sum())

    # Get sum of people in each country in the survey
    sum_people = df['Country'].value_counts()

    # Create new DataFrame from know_python and sum_people series
    new_df = pd.concat([sum_people, know_python], axis='columns', sort=False)
    new_df.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowPython'}, inplace=True)

    # Add new column and insert calculation of percentage of people that know Python in each country
    new_df['PercentWorkWithPython'] = round((new_df['NumKnowPython'] / new_df['NumRespondents']) * 100, 2)

    # Apply filter and sort
    filt = new_df['NumRespondents'] > 5
    new_df = new_df[filt]
    new_df.sort_values(by='PercentWorkWithPython', ascending=False, inplace=True)
    
    print(new_df.head(15))


def salary_calcs(dataframe):
    usd_to_nis = 3.7391
    median = df['SalaryUSD'].median()
    median_nis = int((median * usd_to_nis))

    print(f'\nThe median salary in Israeli Shekels is: {median_nis:,}\n')

def sexuality_count(dataframe):
    sex_count = dataframe['Sexuality'].value_counts()
    print(f'Types of sexualities between the survey participants in Israel:\n{sex_count}\n')

def socmed_count(dataframe):
    socmed_counts = dataframe['SocialMedia'].value_counts()
    print(f'Social media platforms selected as mostly used by survey participants:\n{socmed_counts}\n')

def stats(dataframe):
    salary_calcs(dataframe)
    sexuality_count(dataframe)
    socmed_count(dataframe)

df, schema_df = check_csv(init_work())
df = new_manip(df)
# df = csv_manip(df)
# stats(df)

