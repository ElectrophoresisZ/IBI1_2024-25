import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/Administrator/Desktop/IBI/IBI/IBI1_2024-25/Practical10")

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))
dalys_data.info()
print(dalys_data['DALYs'].describe())
print(dalys_data['Year'].unique())

print(dalys_data.iloc[0,3])
print(dalys_data.iloc[2,0:5])
print(dalys_data.iloc[0:2,:])
print(dalys_data.iloc[0:10:2,0:4])
print(dalys_data.head(10))
print(dalys_data.iloc[9,3])
print(dalys_data.iloc[0:3,[0,1,3]])
my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3,my_columns])

print(dalys_data.loc[2:4,"Year"])
print(dalys_data.loc[dalys_data['Year'] == 1990,"DALYs"])