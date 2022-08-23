import os
import numpy
import pandas as pd

# Change workspace
os.chdir(r'C:\Users\user\Desktop\PyForFun\geopandas\day_1_learning_pandas')
file_list = os.listdir(os.getcwd())
# print(f'Current working directory: {os.getcwd()}')
# print(f'File list:{file_list}')
if len(file_list) == 1 and file_list[0].endswith('.csv'):
    f_path = f'{os.getcwd()}\\{file_list[0]}'

dataframe = pd.read_csv(f_path)
# print(dataframe.shape)
# print('\t')
# print(dataframe.info())

# loop through the table in a col-by-col manner
row_2019 = dict()
row_2020 = dict()
row_2021 = dict()
row_2022 = dict()
row_totals = dict()
yearly_totals = dict()

for num, col in enumerate(dataframe.columns):
    if num == 0:
        # print(f'{col}\n')
        pass
    elif num == (len(dataframe.columns) - 1):
        for i in range(len(col)):
            if yearly_totals:
                yearly_totals[num].append(dataframe[col][i])
            else:
                yearly_totals[num] = [dataframe[col][i]]
    else:
        # print(f'{col}\n{dataframe[col]}\n')
        row_2019[num] = dataframe[col][0]
        row_2020[num] = dataframe[col][1]
        row_2021[num] = dataframe[col][2]
        row_2022[num] = dataframe[col][3]
        row_totals[num] = dataframe[col][4]

for dict in [row_2019, row_2020, row_2021, row_2022, row_totals, yearly_totals]:
    print(dict)

