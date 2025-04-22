## This program hasn't been finished yet.

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# initialize variables
N = 10000

#contact rate
alpha1 = alpha2 = 0.01
# infection rate 
beta = 0.3
delta = 0.001
# recovery rate
gamma1 = 0.05
gamma2 = 0.99

# create arrays to store data
Infected_array = []

# run simulation for different vaccination rates
for j in range(0,11):
    Infected_list = []
    Vaccinated = 0.1*N
    Susceptible = 9999
    Infected_susceptible = 1
    Infected_vaccinated = 0
    Infected = Infected_susceptible + Infected_vaccinated
    Recovered = 0
    Susceptible = int(Susceptible - j * Vaccinated)
    if Susceptible < 0:
        Susceptible = 0
    if Infected < 0:
        Infected = 0
    # run simulation for 1000 time steps
    for i in range(1000):
        contacted_susceptible = np.random.poisson(int(alpha1 * Susceptible),10000)
        contacted_vaccinated = np.random.poisson(int(alpha2 * Vaccinated),10000)
        contacted_susceptible = int(np.mean(contacted_susceptible))
        contacted_vaccinated = int(np.mean(contacted_vaccinated))

        new_infected_susceptible = np.random.choice(range(2), contacted_susceptible, p=[beta, 1-beta])
        new_infected_vaccinated = np.random.choice(range(2), contacted_vaccinated, p=[1-delta, delta])
        new_infected = sum(new_infected_susceptible) + sum(new_infected_vaccinated)
        new_infected_susceptible = int(sum(new_infected_susceptible))
        new_infected_vaccinated = int(sum(new_infected_vaccinated))
        
        new_recovered_susceptible = np.random.choice(range(2), new_infected_susceptible, p=[1-gamma1, gamma1])
        new_recovered_vaccinated = np.random.choice(range(2), new_infected_vaccinated, p=[1-gamma2, gamma2])
        new_recovered = sum(new_recovered_susceptible) + sum(new_recovered_vaccinated)
        
        Susceptible = Susceptible - new_infected 
        Infected = Infected + new_infected - new_recovered
        Recovered = Recovered + new_recovered    
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
plt.figure(figsize=(7,4), dpi=150)
colormap = cm.get_cmap('plasma', 10) 
for i in range(11):
    plt.plot(Infected_array[i], label='Vaccination rate = '+str(i*10)+'%', color=colormap(i))
plt.legend()
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR model with different vaccination rates')
plt.show()
