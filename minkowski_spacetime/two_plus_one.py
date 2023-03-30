import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D spacetime diagram
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the axes labels
ax.set_xlabel('Spatial dimension (x)')
ax.set_ylabel('Spatial dimension (y)')
ax.set_zlabel('Time dimension (t)')

# Plot a stationary worldline (object at x=0, y=0)
t = np.linspace(0, 10, 100)
x = np.zeros_like(t)
y = np.zeros_like(t)
ax.plot(x, y, t, 'b-', label='Stationary worldline')

# Plot a moving worldline (object moving with constant velocity in x and y directions)
x_moving = 0.5 * t
y_moving = 0.3 * t
ax.plot(x_moving, y_moving, t, 'g-', label='Moving worldline')

# Plot an example event (x=2, y=1, t=5)
event_x, event_y, event_t = 2, 1, 5
ax.scatter(event_x, event_y, event_t, c='r', marker='o', label='Event')

# Set the legend and show the plot
ax.legend()
plt.show()
