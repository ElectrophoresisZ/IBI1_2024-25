# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# initialize the population and outbreak
population = np. zeros( (100, 100) )
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# plot the initial outbreak 
plt.figure(figsize=(6,4), dpi = 150)
plt.imshow(population, cmap='viridis', interpolation= 'nearest')
plt.title('Initial Outbreak')
plt.show() 

# define the parameters
beta = 0.3
gamma = 0.05

# simulate the spread of the outbreak
for k in range(1,101):
    # copy the current population
    new_population = population.copy()
    # find the infected people
    rows, cols = np.where(population == 1)
    for i in range(len(rows)):
        row = rows[i]
        col = cols[i]
        # recovery
        if np.random.random() < gamma:
            new_population[row, col] = 2
        # infection
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                # ignore the original point
                if x == 0 and y == 0:
                    continue
                # infect neighboring people
                new_row = row + x
                new_col = col + y
                if new_row >= 0 and new_row < 100 and new_col >= 0 and new_col < 100 and population[new_row, new_col] == 0:
                    if np.random.random() < beta:
                        new_population[new_row, new_col] = 1
        # update the population
        population = new_population.copy()

    # plot the outbreak at different times
    if k in [10, 50, 100]:
        plt.figure(figsize=(6,4), dpi = 150)
        plt.imshow(population, cmap='viridis', interpolation= 'nearest')
        plt.title(f'at {k} times')
        plt.show()
        




