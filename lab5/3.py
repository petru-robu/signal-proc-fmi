import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    contents = np.genfromtxt('Train.csv', delimiter=',')
    ids = contents[:, 0][1:]
    counts = contents[:, 2][1:]
    N = len(ids)
    
    # Sampling rate
    dt = 3600
    fs = 1 / dt

    counts -= np.mean(counts)
    fft_vals = np.fft.fft(counts)
    fft_vals = np.abs(fft_vals) / N
    fft_vals = fft_vals[:N//2]

    fft_freq = np.fft.fftfreq(N, d=dt)[:N//2]

    cnt = 5
    top_idx = np.argsort(fft_vals)[-cnt:][::-1]
    print('Cele mai mari frecvente sunt: ', fft_freq[top_idx])
    
    plt.plot(fft_freq, fft_vals, 'b', label="FFT")
    plt.stem(fft_freq[top_idx], fft_vals[top_idx],linefmt='', markerfmt='kd', basefmt='', label=f"Top {cnt} peaks")
    
    plt.title(f"FFT with removed component)") 
    plt.xlabel('Frecventa (Hz)')
    plt.ylabel('Amplitudine')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig('img/3.svg')
    plt.show()
    
