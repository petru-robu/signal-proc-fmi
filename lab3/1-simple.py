import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    N = 8

    # compute fourier matrix
    n = np.arange(N)
    k = n.reshape((N, 1))
    F = np.exp(-2j * np.pi * k * n / N)

    I_check = F @ F.conj().T
    print(np.allclose(I_check, N*np.eye(N))) 

    fig, axs = plt.subplots(N, 2, figsize=(12, 14))
    for i in range(N):
        axs[i, 0].stem(n, F[i].real)
        axs[i, 0].set_ylabel(f"Re(F[{i}])")
        axs[i, 1].stem(n, F[i].imag)
        axs[i, 1].set_ylabel(f"Im(F[{i}])")
        if i == N-1:
            axs[i, 0].set_xlabel("n")
            axs[i, 1].set_xlabel("n")

    plt.tight_layout()
    plt.savefig("./img/1-simple.svg")
    plt.show()


    