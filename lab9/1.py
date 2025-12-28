import numpy as np
import matplotlib.pyplot as plt

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
plt.plot(x, t, label='series')
plt.plot(x, trend, "r", label='trend', linestyle='--', alpha=0.5)
plt.plot(x, season, "g", label='season', alpha=0.5)
plt.plot(x, residual, "purple", label = 'residuals', alpha=0.3)

plt.legend()
plt.suptitle("Seria de timp")
plt.tight_layout()
plt.savefig("img/1.svg")
plt.show()
