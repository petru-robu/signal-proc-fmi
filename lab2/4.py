import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig, ax = plt.subplots(3, 2, figsize=(12, 10))

    duration = 2
    sr = 44100
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)

    # sine wave 400Hz
    freq = 400
    sine1 = np.sin(2 * np.pi * freq * t)

    # sine wave 800Hz
    freq = 800
    sine2 = np.sin(2 * np.pi * freq * t)

    # sawtooth 400Hz
    freq = 400
    saw = freq * t - np.floor(freq * t)

    # square 800Hz
    freq = 800
    square = 4 * np.floor(freq*t) - 2 * np.floor(2*freq*t) + 1

    ax[0,0].plot(t[:1000], sine1[:1000], 'r')
    ax[0,0].title.set_text('Sine 400Hz')
    ax[1,0].plot(t[:1000], square[:1000], 'b')
    ax[1,0].title.set_text('Square 800Hz')
    ax[2,0].plot(t[:1000], sine1[:1000] + square[:1000], 'purple')
    ax[2,0].title.set_text('Sine 400Hz + Square 800Hz')

    ax[0,1].plot(t[:1000], sine2[:1000], 'r')
    ax[0,1].title.set_text('Sine 800Hz')
    ax[1,1].plot(t[:1000], saw[:1000], 'b')
    ax[1,1].title.set_text('Saw 400Hz')
    ax[2,1].plot(t[:1000], sine2[:1000] + saw[:1000], 'purple')
    ax[2,1].title.set_text('Sine 800Hz + Saw 400Hz')

    fig.suptitle('Adding different signal types', fontsize=16)
    fig.tight_layout()
    plt.savefig("./img/4.svg")
    plt.show()