import numpy as np
import matplotlib.pyplot as plt

colors = {
    0:'r', 1:'g', 2:'b', 3:'y', 4:'purple', 5:'gray', 6:'black'
}

if __name__ == '__main__':
    freq = [20, 70, 100]
    samples = 200
    duration = 0.1
    t = np.linspace(0, 0.1, samples)
    fs = samples/duration

    fig, ax = plt.subplots(3, figsize=(12,9))

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

    dft = np.zeros(samples, dtype=complex)

    for k in range(samples):
        s = 0
        for n in range(samples):
            s += signal[n] * np.exp(-2j * np.pi * k * n / samples)
        dft[k] = np.hypot(np.real(s), np.imag(s))

    smpl =  np.arange(0, samples//2, 1) * fs / samples
    ax[2].stem(smpl, np.abs(dft)[:samples//2] / samples * 2) 
    ax[2].set_title('Discrete ft')

    plt.tight_layout()
    plt.savefig('./img/3.svg')
    plt.show()