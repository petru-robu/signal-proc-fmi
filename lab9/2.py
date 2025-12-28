# exponential smoothing
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

alpha = 0.7 # smoothing factor
s = [t[0]]
for i in range(1, N):
    next = alpha * t[i] + (1 - alpha) * s[i - 1]
    s.append(next)

fig, ax = plt.subplots(2, figsize=(10, 12))

# time series and exponential smoothing
ax[0].plot(x, t, color='green', label='Time Series')
ax[0].plot(x, s, color='orange', linestyle='--', label='Exponential Smoothing')
ax[0].grid(True, linestyle=':', linewidth=0.8)
ax[0].legend(fontsize=12, loc='best')

# zoom-in
ax[1].plot(x[500:600], t[500:600], color='green', label='Time Series')
ax[1].plot(x[500:600], s[500:600], color='orange', linestyle='--', label='Exponential Smoothing alpha=0.7')

alpha = 0.5 # smoothing factor
s = [t[0]]
for i in range(1, N):
    next = alpha * t[i] + (1 - alpha) * s[i - 1]
    s.append(next)
ax[1].plot(x[500:600], s[500:600], color='purple', linestyle='--', label='Exponential Smoothing alpha=0.5')


alpha = 0.3 # smoothing factor
s = [t[0]]
for i in range(1, N):
    next = alpha * t[i] + (1 - alpha) * s[i - 1]
    s.append(next)
ax[1].plot(x[500:600], s[500:600], color='red', linestyle='--', label='Exponential Smoothing alpha=0.3')

ax[1].grid(True, linestyle=':', linewidth=0.8)
ax[1].legend(fontsize=12, loc='best')
plt.tight_layout()
plt.savefig("img/2.svg")    
plt.show()
