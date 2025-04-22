# What does this piece of code do?
# Answer: It randomly produces two integers from 1 to 6 and if the two integers are equal,
#the computer will output the value.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0   #Create a variable and add a value
while progress>=0:
	progress+=1
	first_n = randint(1,6)  #Randomly produce a integer from 1 to 6.
	second_n = randint(1,6)
	if first_n == second_n:  #Compare two integers and output the same value.
		print(progress)
		break  #Jump out of the loop.

