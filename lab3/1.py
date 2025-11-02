import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    samples = 1000
    f = 20 
    t = np.linspace(0, 0.5, 1000)
    sine = np.sin(2 * np.pi * f * t)

    N = 64
    # compute fourier matrix
    n = np.arange(N)
    k = n.reshape((N, 1))
    F = np.exp(-2j * np.pi * k * n / N)

    I_check = F @ F.conj().T
    print(np.allclose(I_check, N*np.eye(N)))

    fig, axs = plt.subplots(6, figsize=(10, 12))
    for i in range(3):
        axs[i].stem(n, F[i].real, 'r')
        axs[i].stem(n, F[i].imag, 'b')
        axs[i].set_title(f"F[{i}]")
        axs[5-i].stem(n, F[N-i-1].real, 'r')
        axs[5-i].stem(n, F[N-i-1].imag, 'b')
        axs[5-i].set_title(f"F[{i}]")
    

    plt.tight_layout()
    plt.savefig("./img/1.svg")
    plt.show()


    