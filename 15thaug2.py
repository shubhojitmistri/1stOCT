import numpy as np
import matplotlib.pyplot as plt

# Parameter t for the curve
t = np.linspace(0, 20*np.pi, 2000)

# Mathematical formula for a jellyfish-like pattern
x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)

# Tentacle-like waves
x_tentacles = np.sin(t*1.5) * 0.3
y_tentacles = -t / (5*np.pi)

# Plot
plt.figure(figsize=(8, 8), facecolor='black')
plt.plot(x, y, color='cyan', linewidth=1.5)
plt.plot(x_tentacles, y_tentacles, color='magenta', alpha=0.6)

plt.axis('off')
plt.title("Mathematical Jellyfish", color='white', fontsize=16)
plt.show()
