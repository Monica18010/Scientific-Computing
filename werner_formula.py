import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(3 * -np.pi, 3 * np.pi, 100)
y = np.linspace(3 * -np.pi, 3 * np.pi, 100)

a = np.sin(x) * 0.8
b = np.sin(y) * 0.5
c = a * b
d = 2 * np.sin((x + y) / 2) * np.cos((x - y) / 2)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines["left"].set_position("center")
ax.spines["bottom"].set_position("center")
ax.spines["right"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

plt.plot(a)
plt.plot(b)
plt.plot(c)
plt.plot(d)

plt.show()
