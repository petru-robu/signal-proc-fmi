import numpy as np
import matplotlib.pyplot as plt
import scipy

def ar_predict_next(series, p):
    N = len(series)
    if N <= p:
        return np.nan
    
    A = np.array([series[i-p:i][::-1] for i in range(p, N)])
    b = series[p:]
    
    # Solve least squares
    coeffs, _, _, _ = scipy.linalg.lstsq(A, b)
    
    # Predict next value using last p observations
    last_p = series[-p:][::-1]
    prediction = np.dot(last_p, coeffs)
    return prediction

def compute_mse(series, p, m):
    N = len(series)
    
    # Skip impossible combinations
    if N <= p or m >= N - p:
        return np.nan
    
    errors = []
    for i in range(N - m, N):
        train_series = series[:i]  # train on all points up to i
        true_value = series[i]
        pred = ar_predict_next(train_series, p)
        errors.append((pred - true_value)**2)
    
    return np.mean(errors)

# Simulate time series
N = 1000
x = np.linspace(0, 5, N)

trend = x*x - x + 1
season = 0.5*np.sin(2*np.pi*2*x) + 0.3*np.sin(2*np.pi*7*x)
residual = 0.2 * np.random.normal(0, 1, N)

series = trend + season + residual

# Hyperparameters
PMIN, PMAX, PSTEP = 1, 100, 5
MMIN, MMAX, MSTEP = 30, 400, 20

p_values = list(range(PMIN, PMAX + 1, PSTEP))
m_values = list(range(MMIN, MMAX + 1, MSTEP))

# Compute error matrix
error_matrix = np.zeros((len(m_values), len(p_values)))

for i, m in enumerate(m_values):
    for j, p in enumerate(p_values):
        error_matrix[i, j] = compute_mse(series, p, m)

plt.figure(figsize=(12, 6))
im = plt.imshow(error_matrix, origin='lower', aspect='auto', cmap='viridis')

plt.xticks(ticks=np.arange(len(p_values)), labels=p_values)
plt.yticks(ticks=np.arange(len(m_values)), labels=m_values)
cbar = plt.colorbar(im)
cbar.set_label("MSE")

for i in range(len(m_values)):
    for j in range(len(p_values)):
        val = error_matrix[i, j]
        if not np.isnan(val):
            color = "white" if val > np.nanmax(error_matrix)/2 else "black"
            # plt.text(j, i, f"{val:.2f}", ha='center', va='center', color=color)

plt.xlabel("AR order p")
plt.ylabel("Evaluation window m")
plt.title("Heatmap of MSE for single-step AR predictions")
plt.show()
plt.savefig('img/4.svg')
