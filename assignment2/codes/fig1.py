import matplotlib.pyplot as plt
import numpy as np

a = 8
d = 8
start_n = -2
end_n = 15

n_values = np.arange(start_n, end_n + 1, 1)
ap_values = np.maximum(0, a + d * n_values)

plt.stem(n_values, ap_values, basefmt='b-', linefmt='d-', markerfmt='ro')
plt.title('Terms of Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('a.png')

