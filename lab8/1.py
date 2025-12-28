import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(4, figsize=(10, 12))


N = 1000
x = np.linspace(0, 5, N)

# trend
trend = x * x - x + 1

# season
f1, f2 = 2, 7
a1, a2 = 0.5, 0.3
season = a1 * np.sin(2 * np.pi * f1 * x) + a2 * np.sin(2 * np.pi * f2 * x)

# residual
mean = 0
std = 1  # standard deviation
residual = np.random.normal(mean, std, size=N)

t = trend + season + 0.2 * residual
ax[0].plot(x, t)
ax[0].set_title("Seria de timp")

ax[1].plot(x, trend, "r")
ax[1].set_title("Trend")

ax[2].plot(x, season, "g")
ax[2].set_title("Season")

ax[3].plot(x, residual, "b")
ax[3].set_title("Residuals")

plt.tight_layout()
plt.savefig("img/1.svg")
plt.show()
