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
x = np.linspace(-5 * rs, 5 * rs, 100)
y = np.linspace(-5 * rs, 5 * rs, 100)

X, Y = np.meshgrid(x, y)

# Plot initial grid
fig, ax = plt.subplots()
ax.set_xlim(-5 * rs, 5 * rs)
ax.set_ylim(-5 * rs, 5 * rs)
ax.set_aspect("equal")

lines = []

for i in range(len(x)):
    line, = ax.plot(x, Y[i, :], color='blue', alpha=0.5)
    lines.append(line)

for i in range(len(y)):
    line, = ax.plot(X[:, i], y, color='blue', alpha=0.5)
    lines.append(line)

# Mark the black hole's position
black_hole_marker, = ax.plot(0, 0, 'ro', markersize=5)

def update(frame):
    factor = frame / 100
    for i in range(len(x)):
        newY = Y[i, :] * (1 - factor * np.exp(-0.5 * (X[i, :] / rs)**2))
        lines[i].set_ydata(newY)

    for i in range(len(y)):
        newX = X[:, i] * (1 - factor * np.exp(-0.5 * (Y[:, i] / rs)**2))
        lines[len(x) + i].set_xdata(newX)

    return lines

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
