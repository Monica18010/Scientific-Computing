# code found on https://www.geeksforgeeks.org/random-walk-implementation-python/
# 2D random walk.
import numpy
import pylab
import random

# number of steps
n = 10000

# creating x,y starting (0,0) coordinates
x = numpy.zeros(n)
y = numpy.zeros(n)

# random variables
for i in range(1, n):
    val = random.randint(1, 4)
    if val == 1:
        x[i] = x[i - 1] + 1  # directions
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1


# plotting random path:
pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
pylab.plot(x, y)
pylab.savefig("rand_walk" + str(n) + ".png", bbox_inches="tight", dpi=600)
pylab.show()
