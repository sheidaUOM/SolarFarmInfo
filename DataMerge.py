#%%
#put all imports here
import pandas as pd
import numpy as np
from datetime import datetime
from os import path

#read data from external files
df1 = pd.read_csv("/Users/sheidashadpour/Desktop/Ekistica_MEI/Dataset/MLF database - latitude and longitude/mlf_database - update for 2020-2021 April 2020.csv")
df2 = pd.read_excel("/Users/sheidashadpour/Desktop/Ekistica_MEI/Dataset/NEM Generation Information Oct 2021.xlsx", sheet_name="ExistingGeneration&NewDevs")

#remove header from AEMO excel file
new_header = df2.iloc[0]
df2 = df2[1:]
df2.columns = new_header

df1 = df1.dropna(subset=['DUID'])
df2 = df2.dropna(subset=['DUID'])
df2 = df2.loc[df2['Unit Status'] == 'In Service']

merge = pd.merge(df1,
                 df2[['DUID', 'Nameplate Capacity (MW)', 'Dispatch Type']],
                 on='DUID')
SolarFarmInfo = merge[['name', 'DUID', 'Latitude', 'Longitude', 'Nameplate Capacity (MW)', 'Dispatch Type']]
#%%
