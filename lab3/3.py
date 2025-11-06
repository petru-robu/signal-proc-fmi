import numpy as np
import matplotlib.pyplot as plt

colors = {
    0:'r', 1:'g', 2:'b', 3:'y', 4:'purple', 5:'gray', 6:'black'
}

def dft_matrix(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    return X

def dft_basic(x):
    N = len(x)
    dft = np.zeros(N, dtype=complex)

    for k in range(N):
        s = 0
        for n in range(N):
            s += x[n] * np.exp(-2j * np.pi * k * n / N)
        dft[k] = np.hypot(np.real(s), np.imag(s))

    return dft
    
# my fft implementation
def my_fft(x):
    N = len(x)  
    if N == 1:
        return x
    X_even = my_fft(x[::2])
    X_odd = my_fft(x[1::2])    
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([X_even + factor[: N//2] * X_odd,
                            X_even + factor[N//2:] * X_odd])


if __name__ == '__main__':
    freq = [20, 70, 100]
    samples = 256
    duration = 0.1
    fs = samples/duration
    t = np.linspace(0, duration, samples)

    fig, ax = plt.subplots(6, figsize=(14,11))
    
    # calculate signal
    signal = np.zeros(samples)
    idx = 0
    for f in freq:
        sine = np.sin(2 * np.pi * f * t)
        ax[0].set_title('Composing freqs sines')
        ax[0].plot(t, sine, colors[idx])
        signal += sine
        idx += 1
    ax[1].set_title('Resulting wave')
    ax[1].plot(t, signal, 'b')

    # calculate dft vectorized
    dft = dft_matrix(signal)
    smpl =  np.arange(0, samples//2, 1) * fs / samples
    ax[2].plot(smpl, np.abs(dft)[:samples//2] / samples * 2, 'r') 
    ax[2].set_title('DFT vectorized result')

    # calculate dft seq
    dft = dft_basic(signal)
    smpl =  np.arange(0, samples//2, 1) * fs / samples
    ax[3].plot(smpl, np.abs(dft)[:samples//2] / samples * 2, 'green') 
    ax[3].set_title('DFT sequential result')

    # calculate dft with np.fft
    dft = np.fft.fft(signal)
    smpl =  np.arange(0, samples//2, 1) * fs / samples
    ax[4].plot(smpl, np.abs(dft)[:samples//2] / samples * 2, 'black') 
    ax[4].set_title('np.fft result')

    # calculate dft with my fft
    dft = my_fft(signal)
    smpl =  np.arange(0, samples//2, 1) * fs / samples
    ax[5].plot(smpl, np.abs(dft)[:samples//2] / samples * 2, 'purple') 
    ax[5].set_title('my fft implementation result')

    plt.tight_layout()
    plt.savefig('./img/3.svg')
    plt.show()