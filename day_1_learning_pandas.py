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

# Below doesn't work, trying to find highest salary per month in all years
if len(row_2019) == len(row_2020) == len(row_2021) == len(row_2022):
    for i in range(1, len(row_2019) - 1):
        check_list = [row_2019.get(i), row_2020.get(i), row_2021.get(i), row_2022.get(i)]
        for num, j in enumerate(check_list):
            if num == 0 and j == numpy.float64():
                month_max = j
            elif j == numpy.float64() and j > month_max:
                month_max = j

        # monthly_max = max(check_list)
        # print(check_list)
        print(f'Highest salary earned in month #{i} is {month_max}\n')