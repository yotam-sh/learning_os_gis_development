import os
# import numpy
# import pandas

# Change workspace
os.chdir(r'C:\Users\user\Desktop\PyForFun\geopandas\day_1_learning_pandas')
file_list = os.listdir(os.getcwd())
print(f'Current working directory: {os.getcwd()}')
print(f'File list:{file_list}')
if len(file_list) == 1 and file_list[0].endswith('.csv'):
    f_path = f'{os.getcwd()}\\{file_list[0]}'

