#import drawing modules
import numpy as np
import matplotlib.pyplot as plt

#create an dictionary called program_language including the data
program_language = {'Java':62.3, 'HTML':52.9, 'Python':51, 'SQL':51, 'TypeScipt':38.5}
#print the dictionary
print(program_language)

#print all the keys and values in the dictionary.
for key in program_language:
    print(key + ':' + str(program_language[key]) + '%')

#create a tuple including all the percentage
percentage = (62.3, 52.9, 51, 51, 38.5)
#create a tuple with five values
ind = np.arange(5)
#draw the bars
plt.bar(ind, percentage, width=0.35)
#change the x variables to 'Java','HTML','Python','SQL','TypeScript'
plt.xticks(ind, ('Java','HTML','Python','SQL','TypeScript'))
#make x,y labels and the title
plt.ylabel('User Percentage/%', size=15)
plt.xlabel('Language Name', size=15)
plt.title('Program Language Popularity', size=20)

#show the picture
plt.show()

#select the program language
select_language = 'select_language'
#print the percentage of the selected language
print('The percentage of developer who uses ' + select_language +' is:' + str(program_language[select_language]) + '%.')




    