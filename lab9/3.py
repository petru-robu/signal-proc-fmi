# moving average model

import numpy as np
import matplotlib.pyplot as plt

def mse(real, pred):
    return np.mean((real - pred) ** 2)

def ma(series, p, theta):
    n = len(series)

    rolling_mean = np.zeros(n)
    predictions = np.zeros(n)
    errs = np.zeros(n)

    # rolling mean
    for t in range(p, n):
        rolling_mean[t] = np.mean(series[t - p : t])

    for t in range(p, n):
        correction = theta * errs[t - 1]
        predictions[t] = rolling_mean[t] + correction
        errs[t] = series[t] - predictions[t]

    return predictions


def find_optimal_ma_params(series):
    best_p = 0
    best_theta = 0.0
    best_mse = float("inf")

    p_values = range(2, 31)
    theta_values = np.linspace(0.0, 1.0, 21)

    for p in p_values:
        for theta in theta_values:
            pred = ma(series, p, theta)

            valid_pred = pred[p:]
            valid_actual = series[p:]

            error = mse(valid_actual, valid_pred)

            if error < best_mse:
                best_mse = error
                best_p = p
                best_theta = theta

    return best_p, best_theta, best_mse


N = 300
x = np.linspace(0, 4, N)

# trend
trend = x * x - x + 1

# season
f1, f2 = 2, 7
a1, a2 = 0.5, 0.3
season = a1 * np.sin(2 * np.pi * f1 * x) + a2 * np.sin(2 * np.pi * f2 * x)

# residual
residual = np.random.normal(0, 1, size=N)

series = trend + season + 0.2 * residual

# MA
best_p, best_theta, best_err = find_optimal_ma_params(series)
print(f"Best MA params: p={best_p}, theta={best_theta:.3f}, MSE={best_err:.4f}")
prediction = ma(series, p=best_p, theta=best_theta)

# plots
fig, ax = plt.subplots(2, figsize=(10, 12))

# original series
ax[0].plot(x, series, color="green", label="Time Series")
ax[0].set_title("Time Series")
ax[0].grid(True, linestyle=":", linewidth=0.8)
ax[0].legend(fontsize=12, loc="best")

# MA prediction
ax[1].plot(x, series, color="green", alpha=0.5, label="Time Series")
ax[1].plot(
    x[best_p:],
    prediction[best_p:],
    color="red",
    linewidth=2,
    label=f"MA Model (p={best_p}, theta={best_theta:.2f})",
)
ax[1].set_title("Optimized Moving Average Model")
ax[1].grid(True, linestyle=":", linewidth=0.8)
ax[1].legend(fontsize=12, loc="best")

plt.tight_layout()
plt.savefig("img/3.svg")
plt.show()
