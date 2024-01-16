import matplotlib.pyplot as plt
import numpy as np

def k_k(a, d, n):
    if n >= 0:
        return a + n * d
    else:
        return 0

def g_g(a, d, start, end):
    n_values = np.arange(start, end + 1, 1)
    ap_values = [k_k(a, d, n) for n in n_values]

    plt.stem(n_values, ap_values, basefmt='b-', linefmt='d-', markerfmt='ro')
    plt.title('Terms of Sequence x(n)')
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.grid(True)
    plt.savefig('a.png')

a = 8
d = 8
start_n = -2
end_n = 15
g_g(a, d, start_n, end_n)

