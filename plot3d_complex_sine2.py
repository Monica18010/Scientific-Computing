#!/usr/bin/env python3
# plot3d_surface.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import sys
import os


def f(x, y):
    return abs(np.sin(x + y * 1j))


def plot(ax):
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-1, 1, 100)

    x, y = np.meshgrid(x, y)

    z = f(x, y)

    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")

    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
