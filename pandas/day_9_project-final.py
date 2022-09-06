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
    schema_csv = 'survey_results_schema.csv'

    print(workdir_files)

load_data()