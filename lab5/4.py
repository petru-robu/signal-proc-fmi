import numpy as np
import matplotlib.pyplot as plt
 
fig, ax = plt.subplots(2, figsize=(10, 9))

# plot data from csv
if __name__ == '__main__':
    contents = np.genfromtxt('Train.csv', delimiter=',')
    
    
    N = 731 # one month
    start = 2075 # monday
    end = start + N
    
    ids = contents[:, 0][start:end]
    counts = contents[:, 2][start:end]
    
    counts -= np.mean(counts)
    fft_vals = np.fft.fft(counts)
    fft_vals = np.abs(fft_vals) / N
    fft_vals = fft_vals[:N//2]

    dt = 3600
    fs = 1 / dt
    fft_freq = np.fft.fftfreq(N, d=dt)[:N//2]
    
    
    ax[0].plot(ids, counts, label='semnalul brut')     
    ax[0].set_title(f"Semnalul brut pe {N} esantioane")
    ax[0].set_xlabel('Esantioane')
    ax[0].set_ylabel('Nr masini')
    ax[0].legend()
    
    ax[1].plot(fft_freq, fft_vals, 'r', label="FFT")
    ax[1].set_title(f"FFT pe {N} esantioane")
    ax[1].set_xlabel('Frecventa [Hz]')
    ax[1].set_ylabel('Amplitudine')
    ax[1].legend()

    fig.tight_layout()
    plt.savefig('img/4.svg')
    plt.show()
