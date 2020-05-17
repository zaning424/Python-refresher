import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()


plt.plot(x, z)
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.show()

