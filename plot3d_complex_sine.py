from pylab import *
from mpl_toolkits.mplot3d import Axes3D

ax = Axes3D(figure(), azim=-110, elev=40)
X = arange(-2.5, 2.5, 0.1)
Y = arange(-1, 1, 0.1)
X, Y = meshgrid(X, Y)
Z = abs(sin(X + Y * 1j))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("abs(sin(x+iy))")
plt.savefig("complex_sin.svg")
plt.show()
