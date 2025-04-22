# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# initialize variables
Susceptible = 9999
Infected = 1
Recovered = 0
N = Susceptible + Infected + Recovered
beta = 0.3
gamma = 0.05

# initialize arrays
Susceptible_array = []
Infected_array = []
Recovered_array = []

# run simulation for 1000 time steps
for i in range(1000):
    up_beta = beta * Infected / N
    new_infected = np.random.choice(range(2), Susceptible, p=[1-up_beta, up_beta])
    new_recovered = np.random.choice(range(2), Infected, p=[1-gamma, gamma])
    Susceptible = Susceptible - sum(new_infected)
    Infected = Infected + sum(new_infected) - sum(new_recovered)
    Recovered = Recovered + sum(new_recovered)
    if Susceptible < 0:
        Susceptible = 0
    if Infected < 0:
        Infected = 0
    Susceptible_array.append(Susceptible)
    Infected_array.append(Infected)
    Recovered_array.append(Recovered)
    
#similar codes for SIR model
'''
Susceptible_array = []
Infected_array = []
Recovered_array = []

for i in range(1000):
    Infected = Infected + beta * Susceptible * Infected / N
    Recovered = Recovered + gamma * Infected
    Susceptible = Susceptible - beta * Susceptible * Infected / N - gamma * Infected
    Infected_array.append(Infected)
    Recovered_array.append(Recovered)
    if Susceptible >= 0:
        Susceptible_array.append(Susceptible)
    else:
        Susceptible_array.append(0)'
'''

# plot results and show the plot
plt.figure(figsize=(7,4), dpi=150)
plt.plot(Susceptible_array, label='Susceptible')
plt.plot(Infected_array, label='Infected')
plt.plot(Recovered_array, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR model')
plt.legend()
plt.savefig('SIR.png')
plt.show()
