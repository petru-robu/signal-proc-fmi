import numpy as np
import matplotlib.pyplot as plt


def create_time_series(x):
    # trend component
    trend = x * x - x + 1

    # seasonal component
    f1, f2 = 2, 7
    a1, a2 = 0.5, 0.3
    season = a1 * np.sin(2 * np.pi * f1 * x) + a2 * np.sin(2 * np.pi * f2 * x)

    # residuals / noise
    residual = np.random.normal(0, 1, size=N)
    residual_mag = 0.7

    series = trend + season + residual_mag * residual
    return series


def mse(real, prediction):
    # mse between series
    return np.mean((real - prediction) ** 2)


def exponential_smoothing(series, alpha):
    s = np.zeros(len(series) - 1)
    s[0] = series[0]
    for i in range(1, len(series) - 1):
        s[i] = alpha * series[i] + (1 - alpha) * s[i - 1]
    return s


def find_best_alpha(series, low=0.0, high=1.0, tol=1e-4):
    best_alpha = 0
    best_mse = float("inf")
    alphas = np.linspace(low, high, 100)

    for alpha in alphas:
        exp = exponential_smoothing(series, alpha)
        curr_mse = mse(series[1:], exp)

        if curr_mse < best_mse:
            best_mse = curr_mse
            best_alpha = alpha

    return best_alpha


def double_exponential_smoothing(series, alpha, beta):
    n = len(series)

    s = np.zeros(n)
    b = np.zeros(n)

    s[0] = series[0]
    b[0] = series[1] - series[0]
    predictions = np.zeros(n)

    predictions[0] = s[0]
    predictions[1] = s[0] + b[0]

    for t in range(1, n - 1):
        s[t] = alpha * series[t] + (1 - alpha) * (s[t - 1] + b[t - 1])
        b[t] = beta * (s[t] - s[t - 1]) + (1 - beta) * b[t - 1]

        predictions[t + 1] = s[t] + b[t]

    return predictions[2:]


def find_best_alpha_beta(
    series, alow=0.01, ahigh=0.99, blow=0.01, bhigh=0.99, steps=20
):
    best = (0, 0)
    best_mse = float("inf")

    alphas = np.linspace(alow, ahigh, steps)
    betas = np.linspace(blow, bhigh, steps)

    for a in alphas:
        for b in betas:
            pred = double_exponential_smoothing(series, a, b)
            curr_mse = mse(series[2:], pred)
            if curr_mse < best_mse:
                best_mse = curr_mse
                best = (a, b)

    return best


def triple_exponential_smoothing(series, alpha, beta, gamma, m):
    n = len(series)

    s = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    predictions = np.zeros(n)

    s[m - 1] = np.mean(series[:m])
    b[m - 1] = (series[m] - series[0]) / m

    for t in range(m):
        c[t] = series[t] - s[m - 1]

    for t in range(m, n):
        predictions[t] = s[t - 1] + b[t - 1] + c[t - m]

        s[t] = alpha * (series[t] - c[t - m]) + (1 - alpha) * (s[t - 1] + b[t - 1])
        b[t] = beta * (s[t] - s[t - 1]) + (1 - beta) * b[t - 1]
        c[t] = gamma * (series[t] - s[t] - b[t - 1]) + (1 - gamma) * c[t - m]

    return predictions


def find_best_alpha_beta_gamma(series, m, steps=10):
    best = (0, 0, 0)
    best_mse = float("inf")

    vals = np.linspace(0.01, 0.99, steps)

    for a in vals:
        for b in vals:
            for g in vals:
                pred = triple_exponential_smoothing(series, a, b, g, m)
                curr_mse = mse(series, pred)
                if curr_mse < best_mse:
                    best_mse = curr_mse
                    best = (a, b, g)

    return best


if __name__ == "__main__":
    # time series
    N = 400
    x = np.linspace(0, 4, N)
    series = create_time_series(x)

    # single MA
    best_alpha = find_best_alpha(series, 0.01, 0.99)
    ema = exponential_smoothing(series, best_alpha)
    print("Best alpha:", best_alpha)

    # double MA
    best_a, best_b = find_best_alpha_beta(series)
    holt = double_exponential_smoothing(series, best_a, best_b)
    print("Best alpha, beta: ", best_a, best_b)

    # triple MA
    m = 20
    best_a3, best_b3, best_g3 = find_best_alpha_beta_gamma(series, m)
    hw = triple_exponential_smoothing(series, best_a3, best_b3, best_g3, m)
    print("Best alpha, beta, gamma:", best_a3, best_b3, best_g3)

    # plots
    fig, ax = plt.subplots(3, figsize=(10, 18))

    # single
    ax[0].plot(x, series, color="green", label="Time Series")
    ax[0].plot(
        x[1:], ema, color="orange", linestyle="--", label="Exponential Smoothing"
    )
    ax[0].set_title(f"Single ES: Best alpha = {best_alpha:.4f}")
    ax[0].grid(True, linestyle=":", linewidth=0.8)
    ax[0].legend(fontsize=12, loc="best")

    # double
    ax[1].plot(x, series, color="green", label="Time Series")
    ax[1].plot(x[2:], holt, color="blue", linestyle="--", label="Holt (Double ES)")
    ax[1].set_title(f"Holt: Best alpha = {best_a:.4f}, beta = {best_b:.4f}")
    ax[1].grid(True, linestyle=":", linewidth=0.8)
    ax[1].legend(fontsize=12, loc="best")

    # triple
    ax[2].plot(x, series, color="green", label="Time Series")
    ax[2].plot(x, hw, color="red", linestyle="--", label="Holt-Winters (Triple ES)")
    ax[2].set_title(
        f"HW: Best alpha = {best_a3:.4f}, beta = {best_b3:.4f}, gamma = {best_g3:.4f}"
    )
    ax[2].grid(True, linestyle=":", linewidth=0.8)
    ax[2].legend(fontsize=12, loc="best")

    # plt.tight_layout()
    plt.savefig("img/2-1.svg")
    plt.show()
