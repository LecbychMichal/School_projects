import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np


def prime():
    i = 2
    n = 10000
    prime = [True for j in range (n + 1)]
    primearray = []
    number = 0

    while i * i <= n:
        if prime[i] == True:
            for j in range(i * i, n + 1, i):
                prime[j] = False

        i += 1
        prime[0] = False
        prime[1] = False

    for i in range(2, n + 1):
        if prime[i]:
            number += 1
            primearray.append(i)

    return primearray, number, n

def ulam_spiral(arr):
    nrows, ncols = arr.shape
    idx = np.arange (nrows * ncols).reshape (nrows, ncols)[::-1]
    spiral_idx = []
    while idx.size:
        spiral_idx.append (idx[0])
        idx = idx[1:]
        idx = idx.T[::-1]

    spiral_idx = np.hstack (spiral_idx)
    spiral = np.empty_like (arr)
    spiral.flat[spiral_idx] = arr.flat[::-1]
    return spiral


primeArray, number, n = prime()
PrimeArray = np.array(primeArray)

w = 100

arr = np.zeros (w ** 2, dtype='u1')
arr[PrimeArray - 1] = 1
arr = ulam_spiral(arr.reshape ((w, w)))

plt.matshow (arr, cmap=cm.binary)
plt.axis ('off')
plt.show ()
print(f"Number of prime numbers up to 10 000 is: {number}")
print(f"Primenumbers:\n {PrimeArray}")



