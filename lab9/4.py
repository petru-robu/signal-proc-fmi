import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from statsmodels.tsa.arima.model import ARIMA

def mse(real, pred):
    return np.mean((real - pred) ** 2)


def arma(series, p, q, phi, theta):
    n = len(series)
    preds = np.zeros(n)
    errs = np.zeros(n)

    for t in range(max(p, q), n):
        ar_part = np.dot(phi, series[t - p : t][::-1])
        ma_part = np.dot(theta, errs[t - q : t][::-1])

        preds[t] = ar_part + ma_part
        errs[t] = series[t] - preds[t]
    return preds


def fit_arma(series, p, q, phi_vals=None, theta_vals=None):
    # find phi and theta coefficients
    if p == 0 and q == 0:
        return np.zeros(len(series)), 0, 0

    phi_vals = (
        phi_vals if phi_vals is not None else [np.linspace(-1, 1, 5) for _ in range(p)]
    )
    theta_vals = (
        theta_vals
        if theta_vals is not None
        else [np.linspace(-1, 1, 5) for _ in range(q)]
    )

    best_err = float("inf")
    best_phi, best_theta = None, None

    # Grid search over all combinations of phi and theta
    phi_combos = list(product(*phi_vals)) if p > 0 else [()]
    theta_combos = list(product(*theta_vals)) if q > 0 else [()]

    for phi_try in phi_combos:
        for theta_try in theta_combos:
            preds = arma(series, p, q, np.array(phi_try), np.array(theta_try))
            start = max(p, q)
            err = mse(series[start:], preds[start:])
            if err < best_err:
                best_err = err
                best_phi = np.array(phi_try)
                best_theta = np.array(theta_try)

    preds = arma(series, p, q, best_phi, best_theta)
    return preds, best_phi, best_theta, best_err


def find_best_pq(series, max_p=5, max_q=5):
    best_p, best_q, best_err = 0, 0, float("inf")
    best_phi, best_theta = None, None

    for p in range(0, max_p + 1):
        for q in range(0, max_q + 1):
            if p == 0 and q == 0:
                continue
            
            preds, phi, theta, err = fit_arma(series, p, q)  # type: ignore
            if err < best_err:
                best_err = err
                best_p, best_q = p, q
                best_phi, best_theta = phi, theta

    return best_p, best_q, best_phi, best_theta, best_err


if __name__ == "__main__":
    # seria de timp
    N = 400
    x = np.linspace(0, 4, N)
    trend = x * x - x + 1
    f1, f2 = 2, 7
    a1, a2 = 0.5, 0.3
    season = a1 * np.sin(2 * np.pi * f1 * x) + a2 * np.sin(2 * np.pi * f2 * x)
    residual = np.random.normal(0, 1, size=N)

    series = trend + season + 0.2 * residual
    eps = series - np.mean(series) # centram seria

    # predictie ARMA
    best_p, best_q, best_phi, best_theta, best_err = find_best_pq(eps, 3, 3)
    print(f"Best ARMA found: p={best_p}, q={best_q}, MSE={best_err:.4f}")
    print(f"phi={best_phi}, theta={best_theta}")
    arma_pred = arma(eps, best_p, best_q, best_phi, best_theta)
    
    # predictie ARIMA 
    arima_model = ARIMA(eps, order=(best_p, 0, best_q))
    arima_fit = arima_model.fit()
    arima_pred = arima_fit.fittedvalues

    # plots 
    plt.figure(figsize=(12, 6))
    plt.plot(eps, label="Serie centrata", color="green")
    start = max(best_p, best_q)
    plt.plot(
        range(start, N),
        arma_pred[start:],
        label=f"ARMA (p={best_p}, q={best_q})",
        color="red",
    )
    plt.plot(
        range(start, N),
        arima_pred[start:],
        label=f"ARIMA statsmodels (p={best_p}, q={best_q})",
        color="blue",
        linestyle="--"
    )
    plt.title("Manual ARMA vs statsmodels ARIMA")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("img/4.svg")
    plt.show()
