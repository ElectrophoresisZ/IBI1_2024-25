# import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# change the working directory to the location of the file
os.chdir("C:/Users/Administrator/Desktop/IBI/IBI/IBI1_2024-25/Practical10")

# read the csv file containing the DALYs data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# print required data
print(dalys_data.iloc[0:10,2])
print('The 10th year of DALYs data for Afghanistan is:', dalys_data.iloc[9,2])
print(dalys_data.loc[dalys_data['Year'] == 1990,"DALYs"])

# collect data for United Kingdom and France
uk = dalys_data.loc[dalys_data['Entity'] == "United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data['Entity'] == "France", ["DALYs", "Year"]]
# calculate the mean DALYs rate for UK and France
uk_mean = uk['DALYs'].mean()
france_mean = france['DALYs'].mean()
print("The mean DALYs rate for United Kingdom is:", uk_mean)
print("The mean DALYs rate for France is:", france_mean)

# compare the mean DALYs rate for UK and France
if uk_mean > france_mean:
    print("United Kingdom has a higher DALYs rate than France")
else:
    print("France has a higher DALYs rate than United Kingdom")

# plot the DALYs rate for UK
plt.plot(uk['Year'], uk['DALYs'], 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs rate for United Kingdom')
plt.show()

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

os.chdir("C:/Users/Administrator/Desktop/IBI/IBI/IBI1_2024-25/Practical10")

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

dalys_data = pd.DataFrame(dalys_data)

# Find the DALYs data bigger than 650000 
print(dalys_data.loc[(dalys_data['Year'] == 1994) & (dalys_data['DALYs'] > 650000), 
                     ['Year', 'Entity', 'DALYs']])
# Descriptive statistics of DALYs data for each year
print(dalys_data.groupby('Year')['DALYs'].describe())

# Draw boxplots of DALYs data for each year
sns.set_style(style="whitegrid")
sns.boxplot(x='Year', y='DALYs', data=dalys_data, 
            palette="colorblind", width=0.5, showfliers=False)
plt.title('Boxplot of DALYs (Filter Outliers)')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.xticks(rotation=90)
plt.figure(figsize=(12,10))
plt.show()