import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/Administrator/Desktop/IBI/IBI/IBI1_2024-25/Practical10")

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

'''
uk = dalys_data.loc[dalys_data['Entity'] == "United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data['Entity'] == "France", ["DALYs", "Year"]]
uk_mean = uk['DALYs'].mean()
france_mean = france['DALYs'].mean()
if uk_mean > france_mean:
    print("United Kingdom has a higher DALYs rate than France")
else:
    print("France has a higher DALYs rate than United Kingdom")

plt.plot(uk['Year'], uk['DALYs'], 'b+')
#plt.plot(uk['Year'], uk['DALYs'], 'r+')
#plt.plot(uk['Year'], uk['DALYs'], 'bo')
plt.xticks(uk.Year,rotation=-90)
plt.show()
'''


