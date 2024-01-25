import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
data = np.loadtxt("data.txt")
n_values, ap_values = data[:, 0], data[:, 1]

# Plot the data
plt.stem(n_values, ap_values, basefmt='b-', linefmt='d-', markerfmt='ro')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)

# Save the plot as an image file
plt.savefig('a.png')
