import matplotlib.pyplot as plt
import sympy
import numpy as np

a_val = np.linspace(0, 20)


def exp_pdf(lam, a):

    return lam * np.exp(-lam * a)


b_val1 = np.array([exp_pdf(1.0, a) for a in a_val])

b_val2 = np.array([exp_pdf(2.0, a) for a in a_val])

b_val3 = np.array([exp_pdf(5.0, a) for a in a_val])

fig, aa = plt.subplots(figsize=(15, 15))

aa.plot(a_val, b_val1, label="lambda=1.0")

aa.plot(a_val, b_val2, label="lambda = 2.0")

aa.plot(a_val, b_val3, label="lambda = 5.0")

plt.show()
