import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, figsize=(10, 12))

N = 1000
x = np.linspace(0, 5, N)

# trend
trend = x * x - x + 1

# season
f1, f2 = 2, 7
a1, a2 = 1.5, 1.3
season = a1 * np.sin(2 * np.pi * f1 * x) + a2 * np.sin(2 * np.pi * f2 * x)

# residual
mean = 0
std = 1  # standard deviation
residual = np.random.normal(mean, std, size=N)

t = trend + season + 0.5 * residual
ax[0].plot(x, t)
ax[0].set_title("Seria de timp")

autocorr = np.convolve(t, t[::-1], mode="full")
autocorr /= np.max(autocorr)
ax[1].plot(x, autocorr[len(autocorr)//2:])
ax[1].set_title("Autocorelatia")

print(autocorr)
plt.tight_layout()
plt.savefig("img/2.svg")
plt.show()
