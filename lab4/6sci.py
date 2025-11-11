import numpy as np
import matplotlib.pyplot as plt
import scipy

def stereoToMono(sgn):
    if sgn.ndim == 2:
        return sgn.mean(axis=1)

if __name__ == '__main__':
    audio_path = './audio/cargo.wav'
    rate, sgn = scipy.io.wavfile.read(audio_path)
    sgn = stereoToMono(sgn).astype(np.float32)
    sgn = sgn[::16] # decimam semnalul

    N = len(sgn) 
    group_size = 256
    step = group_size // 2 

    print(f"Signal length: {N}\nGroup size: {group_size}")
    
    f, t, Sxx = scipy.signal.spectrogram(sgn, fs=rate, nperseg=group_size, noverlap=step)

    Sxx_ds = Sxx[::4, ::4]  # decimam spectograma
    f_ds = f[::4]
    t_ds = t[::4]
    
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(t_ds, f_ds, 10*np.log10(Sxx_ds + 1e-6), shading='auto')
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency [Hz]')
    plt.colorbar(label='Magnitude [dB]')
    plt.tight_layout()
    plt.savefig('./img/6sci.svg', dpi=72) 
    plt.show()
