import numpy as np
import matplotlib.pyplot as plt
import scipy

def ar(series, p, m):
    # m se numeste orizontul de timp
    # p este dimensiunea modelului AR
    N = len(series)

    A = [] # design matrix
    b = series[N - m : N] # last m values of series

    for i in range(N - m, N):
        prev_values = series[i - p : i][::-1] # prev p values 
        row = prev_values 
        A.append(row)

    A = np.array(A)
    print(A)
    
    coeffs, _, _, _ = scipy.linalg.lstsq(A, b) 

    prediction = A @ coeffs # prediction for the last m values
    return np.arange(N - m, N), prediction

#----calculate time series----
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
std = 1 # standard deviation  
residual = np.random.normal(mean, std, size=N)
series = trend + season + 0.2 * residual

#----calculate ar model for p and m
p, m = 15, 400
t, pred = ar(series, p, m)

#---plot---
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(t, series[N - m:], color="tab:green", linewidth=2, label="Time Series")

ax.plot(t, pred, color="tab:red", linewidth=2, linestyle="--", alpha=0.7, label="AR prediction")

ax.set_title(f"AR prediction (p={p}, m={m})", fontsize=14)
ax.set_xlabel("Timp")
ax.set_ylabel("Amplitudine")
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="best")

plt.tight_layout()
plt.savefig("img/3.svg")
plt.show()