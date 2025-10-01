# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Change the size of the graph using figsize
fig = plt.figure(figsize=(10, 10))

# Generating a 3D sine wave
ax = fig.add_subplot(111, projection='3d')

# Assigning coordinates
x = np.linspace(-1, 5, 10)
y = np.linspace(-1, 5, 10)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Creating the visualization
ax.plot_wireframe(X, Y, Z, color='green')

# Turn off/on axis
plt.axis('off')

plt.show()
