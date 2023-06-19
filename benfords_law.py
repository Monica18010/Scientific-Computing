from random import choices
from collections import Counter
import matplotlib.pyplot as plt

population = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# these are the Benford's Law percentage weights)
weights = [0.301, 0.176, 0.124, 0.096, 0.079, 0.066, 0.057, 0.054, 0.047]

# generate probable first digits in the set of Benford's distribution

first_digits = choices(population, weights, k=10**5)

values_in_order = Counter(first_digits).most_common()
[print(i) for i in values_in_order]

number_set = []


count = []
for c in values_in_order:
    count.append(c[1])

y_pos = population

plt.figure(figsize=(10, 10))
# chart axis labels
plt.xticks(y_pos, population)
plt.ylabel("Leading Digit Count")
plt.xlabel("Digit")
plt.title("Benford's Law")


# Plot bars and color
plt.bar(y_pos, count, color="violet")

# Limit for the Y axis
plt.ylim(0, int(max(count) * 1.1))

# Display histogram
plt.show()
