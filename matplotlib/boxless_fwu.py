from matplotlib import cm                   # Colour gradient (colormap)
import matplotlib.pyplot as plt             # Generate plots
from mpl_toolkits.mplot3d import Axes3D     # Have a 3D env

# Define the variables
import numpy as np
interval = np.linspace(-1,1,32)
x,y = np.meshgrid(interval,interval)

# More information:
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
# https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html

# Define the parametric equations
X=x
Y=y*y       # Alternative: np.power(y,2)
Z=x*y*y*y   # Alternative: x*np.power(y,3)

fig = plt.figure()      # Generate a figure called "fig"

ax = fig.add_subplot(projection='3d')
ax.axis('off')          # Hide the "background box"
ax.plot_surface(X,Y,Z, cmap=cm.ocean)
fig.show()              # Show "fig"

# You can also save it without interacting with the window:
fig.savefig('folded_umbrella.eps')
