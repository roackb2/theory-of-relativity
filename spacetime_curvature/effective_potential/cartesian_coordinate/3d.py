import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
mass = 1.0
G = 1.0
c = 1.0

# Schwarzschild radius
rs = 2 * G * mass / c**2

# Define grid of Cartesian coordinates
x = np.linspace(-5 * rs, 5 * rs, 100)
y = np.linspace(-5 * rs, 5 * rs, 100)

X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# Calculate the effective potential for each grid point
V_eff = -G * mass / R - 0.5 * G**2 * mass**2 / (R * c**2)

# Normalize the effective potential
V_eff_norm = (V_eff - V_eff.min()) / (V_eff.max() - V_eff.min())

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, V_eff_norm, cmap='viridis', alpha=0.8)
ax.set_title("Spacetime Curvature near a Black Hole")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Normalized Effective Potential")

plt.show()