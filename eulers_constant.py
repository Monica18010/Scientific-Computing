import math as m
import numpy as np
import matplotlib.pyplot as plt

# Euler's constant
EulerMascheroniApp = round((1.0 - m.gamma(1 + 1.0e-8)) * 1.0e14) * 1.0e-6
print(EulerMascheroniApp)


harmonic_numbers = []
x = []
value = 0
gamma = 0.5772156649


fn = []

# generate the first 50 harmonic numbers
for i in range(1, 51):

    value = value + (1 / i)
    harmonic_numbers.append(value)

    # function (gamma) +ln(x)
    function_value = (gamma) + m.log(i)
    fn.append(function_value)
    x.append(i)

# Plot step and line graph
plt.plot(x, fn, "r")
plt.step(x, harmonic_numbers)
plt.legend(["(gamma) +ln(x)", "Harmonic numbers"])
plt.show()
