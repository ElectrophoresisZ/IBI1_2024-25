# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# initialize variables
N = 10000
Vaccinated = 0.1*N
Susceptible = 9999
Infected = 1
Recovered = 0
beta = 0.3
gamma = 0.05

# create arrays to store data
Infected_array = []

# run simulation for different vaccination rates
for j in range(0,11):
    Infected_list = []
    Vaccinated = 0.1*N
    Susceptible = 9999
    Infected = 1
    Recovered = 0
    Susceptible = int(Susceptible - j * Vaccinated)
    if Susceptible < 0:
        Susceptible = 0
    if Infected < 0:
        Infected = 0
    # run simulation for 1000 time steps
    for i in range(1000):
        up_beta = beta * Infected / N
        new_infected = np.random.choice(range(2), Susceptible, p=[1-up_beta, up_beta])
        new_recovered = np.random.choice(range(2), Infected, p=[1-gamma, gamma])
        Susceptible = Susceptible - sum(new_infected) 
        Infected = Infected + sum(new_infected) - sum(new_recovered)
        Recovered = Recovered + sum(new_recovered)    
        Infected_list.append(Infected)
    Infected_array.append(Infected_list)

# similar codes for SIR model with vaccination
'''
Infected_array = []

for j in range(1,11):
    Infected_list = []
    Vaccinated = 0.1*N
    Susceptible = 9999
    Infected = 1
    Recovered = 0
    Susceptible = Susceptible - j * Vaccinated
    for i in range(1000):
        Infected = Infected + beta * Susceptible * Infected / N
        Recovered = Recovered + gamma * Infected
        Susceptible = Susceptible - beta * Susceptible * Infected / N - gamma * Infected
        Infected_list.append(Infected)
    Infected_array.append(Infected_list)
'''

# plot the results and show the plot
plt.figure(figsize=(7,4),dpi=150)
colormap = cm.get_cmap('plasma', 10) 
for i in range(11):
    plt.plot(Infected_array[i], label='Vaccination rate = '+str(i*10)+'%', color=colormap(i))
plt.legend()
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR model with different vaccination rates')
plt.show()
