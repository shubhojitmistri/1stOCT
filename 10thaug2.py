import numpy as np
import matplotlib.pyplot as plt

# Create sphere coordinates
phi = np.linspace(0, np.pi, 50)      # polar angle
theta = np.linspace(0, 2 * np.pi, 50) # azimuthal angle
phi, theta = np.meshgrid(phi, theta)

# Radius of sphere
r = 1

# Parametric equations for sphere
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='skyblue', edgecolor='k')

# Set labels
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title("3D Sphere")

plt.show()