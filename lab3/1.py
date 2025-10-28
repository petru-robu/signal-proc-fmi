import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # sampled signal
    x = np.linspace(0, 0.05, 8)
    sin = np.sin(200 * np.pi * x)

    # compute dft
    N = 8
    dft = np.zeros(N, dtype=complex)

    for k in range(N):
        s = 0
        for n in range(N):
            s += sin[n] * np.exp(-2j * np.pi * k * n / N)
        dft[k] = s
    print(dft)
    
    # compute fourier matrix
    n = np.arange(N)
    k = n.reshape((N, 1))
    F = np.exp(-2j * np.pi * k * n / N)

    I_check = F @ F.conj().T
    print(np.allclose(I_check, N*np.eye(N))) 

    fig, axs = plt.subplots(N, 2, figsize=(10, 12))
    for i in range(N):
        axs[i, 0].stem(n, F[i].real, use_line_collection=True)
        axs[i, 0].set_ylabel(f"Re(F[{i}])")
        axs[i, 1].stem(n, F[i].imag, use_line_collection=True)
        axs[i, 1].set_ylabel(f"Im(F[{i}])")
        if i == N-1:
            axs[i, 0].set_xlabel("n")
            axs[i, 1].set_xlabel("n")

    plt.tight_layout()
    plt.show()


    