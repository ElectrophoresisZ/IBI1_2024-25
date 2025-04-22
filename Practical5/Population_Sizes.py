# import necessary libraries
import matplotlib.pyplot as plt

UK_countries = [57.11, 3.13, 1.91, 5.45]
China_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
UK_countries.sort()
China_provinces.sort()

print(UK_countries)
print(China_provinces)

def list_percentage_calculator(list):
    total = 0
    percentage_list = []
    for i in list:
        total = total + i
    for j in list:
        percentage_list.append(round(j/total*100, 2))
    return percentage_list

UK_countries_percentage = list_percentage_calculator(UK_countries)
China_provinces_percentage = list_percentage_calculator(China_provinces)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) 

labels = ['Northern Ireland','Wales','Scotland','England']
sizes = UK_countries_percentage
explode = (0.25,0.1,0.1,0)
colors = ['#999999', '#E69F00', '#56B4E9', '#009E73']
ax1.pie(sizes, explode = explode, labels = labels, 
        autopct = '%1.1f%%', colors = colors, 
        shadow = False, startangle = 90)
ax1.axis('equal')

labels = ['Fujian','Jiangxi','Anhui','Zhejiang','Jiangsu']
sizes = China_provinces_percentage
explode = (0.1,0.1,0,0,0.05)
colors = ['#999999', '#E69F00', '#56B4E9', '#009E73', '#F0E442']
ax2.pie(sizes, explode = explode, labels = labels,
        autopct = '%1.1f%%', colors = colors, 
        shadow = False, startangle = 90)
ax2.axis('equal')

plt.tight_layout()
plt.show()

