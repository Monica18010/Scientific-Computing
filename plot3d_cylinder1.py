import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")


# Cylinder
x = np.linspace(-1, 1, 100)
z = np.linspace(-1, 1, 100)
Xc, Zc = np.meshgrid(x, z)
Yc = np.sqrt(1 - Xc**2)

# Draw parameters
rstride = 30
cstride = 10
ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)
ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)
ax.plot_wireframe(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
