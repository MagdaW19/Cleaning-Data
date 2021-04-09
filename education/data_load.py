# Copyright 2021 Magda Wójcicka

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Script that loads data and saves processed version.
"""

# Basic imports
import numpy as np 
import pandas as pd 

# Additional imports
import os
from education.utils import fix_census_date, is_country

# Paths
raw_data = '../data/raw'
processed_data = '../data/processed'

# Get all files with data
file_list = os.listdir(raw_data)
file_names = ['ED_CS', 'ED_C', 'ED_D', 'ED_FN', 'ED_S']

# Loading data
data_dict = {}

for path, name in zip(file_list, file_names):
    file_path = os.path.join(raw_data, path)
    data_dict[name] = pd.read_csv(file_path)

# File with information about data sources
# Removing last column that is fully empty
data_dict['ED_CS'].drop(columns=['Unnamed: 3'], inplace = True)

# Saving processed file
edcs_new_path = os.path.join(processed_data, 'data_sources.csv')
data_dict['ED_CS'].to_csv(edcs_new_path,index=False)


# File with info about countries
# creating column with info if entity is country or region/group
data_dict['ED_C']['Is_Country']=data_dict['ED_C']['Short Name'].apply(is_country)

# Fixing census year which includes notes and year values
data_dict['ED_C']['POP_census_year'] = data_dict['ED_C']['Latest population census'].apply(fix_census_date)

# Columns to keep
ED_C_cols = ['Country Code','Short Name','Region','Income Group','POP_census_year', 'Is_Country']

# Saving file
edc_new_path = os.path.join(processed_data, 'countries_info.csv')
data_dict['ED_C'][ED_C_cols].to_csv(edc_new_path,index=False)

# File with data_series code explanation
data_dict['ED_S'].dropna(axis=1, how='all', inplace=True)
ED_S_cols = ['Series Code', 'Topic', 'Indicator Name', 'Long definition', 'Source']

# Save the file
eds_new_path = os.path.join(processed_data, 'data_explain.csv')
data_dict['ED_S'][ED_S_cols].to_csv(eds_new_path,index=False)

# File with data series code, year and source description
data_dict['ED_FN'].drop(columns=['Unnamed: 4'], inplace=True)
data_dict['ED_FN']['Year'] = data_dict['ED_FN']['Year'].apply(lambda x: x[2:])

# Save file
edfn_new_path = os.path.join(processed_data, 'data_year.csv')
data_dict['ED_FN'].to_csv(edfn_new_path,index=False)

# Saving data
data_dict['ED_D'].drop(columns=['Unnamed: 69'], inplace=True)
edd_new_path = os.path.join(processed_data, 'ed_data.csv')
data_dict['ED_D'].to_csv(edd_new_path,index=False)
