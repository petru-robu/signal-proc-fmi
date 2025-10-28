import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(2)

if __name__ == '__main__':

    f1, f2, f3, f4 = 20, 30, 70, 330
    N = 5000

    x = np.linspace(0, 1, N)
    signal = np.sin(2*f1*np.pi*x) + np.sin(2*f2*np.pi*x) + np.sin(2*f3*np.pi*x) + np.sin(2*f4*np.pi*x)

    ax[0].plot(x, signal)


    dft = np.zeros(N, dtype=complex)

    for k in range(N):
        s = 0
        for n in range(N):
            s += signal[n] * np.exp(-2j * np.pi * k * n / N)
        dft[k] = np.hypot(np.real(s), np.imag(s))
    #print(dft)


    smpl =  np.arange(0, N//2, 1)
    ax[1].stem(smpl, np.abs(dft)[:N//2])


    plt.show()