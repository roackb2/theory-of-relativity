import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
mass = 1.0
G = 1.0
c = 1.0

# Schwarzschild radius
rs = 2 * G * mass / c**2

# Define grid of Cartesian coordinates
x = np.linspace(-5 * rs, 5 * rs, 200)
y = np.linspace(-5 * rs, 5 * rs, 200)

X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# Calculate the effective potential for each grid point
V_eff = -G * mass / R - 0.5 * G**2 * mass**2 / (R * c**2)

# Normalize the effective potential
V_eff_norm = (V_eff - V_eff.min()) / (V_eff.max() - V_eff.min())

# Create the plot
fig, ax = plt.subplots()
im = ax.imshow(V_eff_norm, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', animated=True)
cbar = plt.colorbar(im)
cbar.set_label('Normalized Effective Potential')

def update(frame):
    global V_eff_norm
    # Shift the effective potential to create the appearance of time evolution
    V_eff_norm = np.roll(V_eff_norm, 1, axis=1)
    im.set_array(V_eff_norm)
    return im,

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
