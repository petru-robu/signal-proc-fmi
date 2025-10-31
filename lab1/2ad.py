import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig, ax = plt.subplots(4)

    freq = 400
    samples = 1600
    t = np.linspace(0, 0.025, samples)
    x = np.sin(2 * np.pi * freq * t)
    ax[0].plot(t, x, 'b')
    ax[0].title.set_text("Sinusoidal 400Hz 1600samples")

    freq = 800
    samples = 400
    t = np.linspace(0, 3, samples)
    x = np.sin(2 * np.pi * freq * t)
    ax[1].plot(t, x, 'b')
    ax[1].title.set_text("Sinusoidal 800Hz 3sec")

    freq = 240
    samples = 1000
    t = np.linspace(0, 0.025, samples)
    x = freq * t - np.floor(freq * t)
    ax[2].plot(t, x, 'b')
    ax[2].title.set_text("Sawtooth 240Hz")

    freq = 300
    samples = 1000
    t = np.linspace(0, 0.025, samples)
    x = 4 * np.floor(freq*t) - 2 * np.floor(2*freq*t) + 1
    ax[3].plot(t, x, 'b')
    ax[3].title.set_text("Square 300Hz")

    fig.tight_layout()
    plt.savefig("./img/2ad.svg")
    plt.show()
