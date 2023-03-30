import numpy as np
import matplotlib.pyplot as plt

# Parameters
mass = 1.0
G = 1.0
c = 1.0

# Schwarzschild radius
rs = 2 * G * mass / c**2

# Define grid of polar coordinates
r = np.linspace(rs * 1.001, 5 * rs, 200)
theta = np.linspace(0, 2 * np.pi, 200)

R, Theta = np.meshgrid(r, theta)

# Calculate the effective potential for each grid point
V_eff = -G * mass / R - 0.5 * G**2 * mass**2 / (R * c**2)

# Normalize the effective potential
V_eff_norm = (V_eff - V_eff.min()) / (V_eff.max() - V_eff.min())

# Plot the spacetime curvature
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
scatter = ax.scatter(Theta, R, c=V_eff_norm, cmap='viridis', s=1)

# Mark the Schwarzschild radius
ax.plot([0, 2 * np.pi], [rs, rs], 'r--', label='Schwarzschild radius')

ax.set_title("Spacetime Curvature near a Black Hole")
ax.set_rticks([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.legend()

# Optional: Add a colorbar
cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Normalized Effective Potential')

plt.show()
