import numpy as np
import matplotlib.pyplot as plt

# 𝑟=𝜃 as it rotates from 0≤𝜃≤8𝜋
theta = np.linspace(0.0, 8 * np.pi, 1000)
a, b = 0, 2.0
plt.polar(theta, a + b * theta)
plt.show()
