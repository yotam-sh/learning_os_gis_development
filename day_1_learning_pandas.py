import os
import numpy
import pandas as pd

# Change workspace
os.chdir(r'C:\Users\user\Desktop\PyForFun\geopandas\day_1_learning_pandas')
file_list = os.listdir(os.getcwd())
print(f'Current working directory: {os.getcwd()}')
print(f'File list:{file_list}')
if len(file_list) == 1 and file_list[0].endswith('.csv'):
    f_path = f'{os.getcwd()}\\{file_list[0]}'

dataframe = pd.read_csv(f_path)
# print(dataframe.shape)
# print('\t')
# print(dataframe.info())

# loop through the table in a col-by-col manner
for num, col in enumerate(dataframe.columns):
    if num == 0:
        print(f'{col}\n')
    else:
        print(f'{col}\n{dataframe[col]}\n')
