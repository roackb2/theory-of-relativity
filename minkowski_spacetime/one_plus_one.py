import numpy as np
import matplotlib.pyplot as plt

# Define a function to plot light cones
def plot_light_cones(ax, x, t):
    ax.plot([x - t, x + t], [0, t], 'r--', alpha=0.5)
    ax.plot([x + t, x - t], [0, t], 'r--', alpha=0.5)

# Create a spacetime diagram
fig, ax = plt.subplots()

# Set the axes labels
ax.set_xlabel('Spatial dimension (x)')
ax.set_ylabel('Time dimension (t)')

# Plot a stationary worldline (object at x = 0)
ax.plot([0, 0], [0, 10], 'b-', label='Stationary worldline')

# Plot a moving worldline (object moving with constant velocity)
t = np.linspace(0, 10, 100)
x = 0.5 * t
ax.plot(x, t, 'g-', label='Moving worldline')

# Plot light cones for an event at (x=2, t=5)
event_x, event_t = 2, 5
ax.plot(event_x, event_t, 'ro', label='Event')
plot_light_cones(ax, event_x, event_t)

# Set the legend and show the plot
ax.legend()
plt.show()
