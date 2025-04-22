import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation

# 初始化变量
N = 10000
grid_size = int(np.sqrt(N))  # 假设是一个正方形网格
assert grid_size**2 == N, "N 必须是一个完全平方数"

# 接触率
alpha1 = alpha2 = 0.01
# 感染率
beta = 0.3
delta = 0.001
# 恢复率
gamma1 = 0.05
gamma2 = 0.8

# 定义相邻个体的偏移量
neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 运行不同疫苗接种率的模拟
for j in range(0, 11):
    Infected_list = []
    grid_states = []  # 用于记录每个时间步的网格状态

    # 初始化网格
    grid = np.zeros((grid_size, grid_size), dtype=int)
    # 随机选择一个初始感染个体
    infected_x, infected_y = np.random.randint(0, grid_size, 2)
    grid[infected_x, infected_y] = 1
    Vaccinated = int(0.1 * N)
    # 随机选择接种疫苗的个体
    vaccinated_indices = np.random.choice(N, Vaccinated, replace=False)
    vaccinated_x = vaccinated_indices // grid_size
    vaccinated_y = vaccinated_indices % grid_size
    for x, y in zip(vaccinated_x, vaccinated_y):
        if grid[x, y] == 0:
            grid[x, y] = 2  # 2 表示接种疫苗的个体

    Susceptible = N - np.sum(grid > 0)
    Infected = np.sum(grid == 1)
    Recovered = 0

    # 减少易感个体数量
    Susceptible = int(Susceptible - j * Vaccinated)
    if Susceptible < 0:
        Susceptible = 0
    if Infected < 0:
        Infected = 0

    # 运行 1000 个时间步的模拟
    for i in range(1000):
        new_infected = 0
        new_recovered = 0
        new_grid = grid.copy()
        for x in range(grid_size):
            for y in range(grid_size):
                if grid[x, y] == 0:  # 易感个体
                    contacted = 0
                    for dx, dy in neighbors:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx, ny] == 1:
                            contacted += 1
                    if contacted > 0:
                        new_infected_susceptible = np.random.choice(
                            range(2), contacted, p=[beta, 1 - beta])
                        if sum(new_infected_susceptible) > 0:
                            new_grid[x, y] = 1
                            new_infected += 1
                elif grid[x, y] == 1:  # 感染个体
                    new_recovered_susceptible = np.random.choice(
                        range(2), 1, p=[1 - gamma1, gamma1])
                    if sum(new_recovered_susceptible) > 0:
                        new_grid[x, y] = 3  # 3 表示康复个体
                        new_recovered += 1
                elif grid[x, y] == 2:  # 接种疫苗的个体
                    contacted = 0
                    for dx, dy in neighbors:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx, ny] == 1:
                            contacted += 1
                    if contacted > 0:
                        new_infected_vaccinated = np.random.choice(
                            range(2), contacted, p=[1 - delta, delta])
                        if sum(new_infected_vaccinated) > 0:
                            new_grid[x, y] = 1
                            new_infected += 1
        grid = new_grid
        Susceptible = np.sum(grid == 0)
        Infected = np.sum(grid == 1)
        Recovered = np.sum(grid == 3)
        Infected_list.append(Infected)
        grid_states.append(grid.copy())

    # 绘制感染人数随时间变化的曲线
    plt.figure(figsize=(7, 4), dpi=150)
    plt.plot(Infected_list, label='Vaccination rate = '+str(j * 10)+'%')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Number of Infected People')
    plt.title('Spatial SIR model with vaccination rate of '+str(j * 10)+'%')
    plt.show()

    # 绘制空间分布图动画
    fig, ax = plt.subplots()
    img = ax.imshow(grid_states[0], cmap='viridis', interpolation='nearest')
    ax.set_title('Spatial Distribution at Time Step 0')

    def update(frame):
        img.set_data(grid_states[frame])
        ax.set_title(f'Spatial Distribution at Time Step {frame}')
        return img,

    ani = FuncAnimation(fig, update, frames=len(grid_states), interval=100, blit=True)
    plt.show()
