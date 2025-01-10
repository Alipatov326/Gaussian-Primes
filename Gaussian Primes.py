import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter the upper/lower bound for a and b: "))
coords = np.array([])
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def findGaussianPrimes(N):
    coords = np.array([])
    for i in range(-N, N):
        for k in range(-N, N):
            if i != 0 and k != 0 and isPrime(i**2 + k**2) and (i**2 + k**2)%4 != 3:
                coords = np.append(coords, i + k * 1j)
            elif i == 0 and isPrime(abs(k)) and abs(k)%4 == 3:
                coords = np.append(coords, i + k * 1j)
            elif k == 0 and isPrime(abs(i)) and abs(i)%4 == 3:
                coords = np.append(coords, i + k * 1j)
    return coords

coords = findGaussianPrimes(N)
x = coords.real
y = coords.imag

markerSize = 10 / (N**.5)
plt.gca().set_aspect(1.0)
plt.scatter(x, y, color="purple", marker="s", s=markerSize)
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()