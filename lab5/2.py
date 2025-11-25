import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(2, figsize=(10, 9))

if __name__ == '__main__':
    contents = np.genfromtxt('Train.csv', delimiter=',')
    ids = contents[:, 0][1:]
    counts = contents[:, 2][1:]
    N = len(ids)

    # Sampling rate
    dt = 3600
    fs = 1 / dt

    # FFT
    fft_vals = np.fft.fft(counts)
    fft_vals = np.abs(fft_vals) / N
    fft_vals = fft_vals[:N//2]

    fft_freq = np.fft.fftfreq(N, d=dt)[:N//2]
    dc = fft_vals[0]

    ax[0].set_title("FFT without removed component")
    ax[0].plot(fft_freq, fft_vals, 'r')
    ax[0].set_xlabel('Frecventa (Hz)')
    ax[0].set_ylabel('Amplitudine')
    ax[0].legend()
    ax[0].grid(True)

    counts -= np.mean(counts)
    fft_vals = np.fft.fft(counts)
    fft_vals = np.abs(fft_vals) / N
    fft_vals = fft_vals[:N//2]

    fft_freq = np.fft.fftfreq(N, d=dt)[:N//2]

    ax[1].set_title(f"FFT with removed component (Comp value in freq: {dc})")
    ax[1].plot(fft_freq, fft_vals, 'b')
    ax[1].set_xlabel('Frecventa (Hz)')
    ax[1].set_ylabel('Amplitudine')
    ax[1].grid(True)

    fig.tight_layout()
    plt.savefig('img/2.svg')
    plt.show()
    
