'''import matplotlib.pyplot as plt
import numpy as np

N = 10
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x, y, marker = 'o')
plt.show()'''

L = [2,1,3]
print(L)
L1 = L.append(5)
L2 = [4,6,7]  
print(L1)      
print(L.extend(L2))