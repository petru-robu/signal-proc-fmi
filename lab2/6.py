import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fs = 500
    t = np.linspace(0, 0.015, fs)

    sine1 = np.sin(2 * np.pi * (fs / 2) * t)
    sine2 = np.sin(2 * np.pi * (fs / 4) * t)
    sine3 = np.sin(2 * np.pi * (0) * t)

    fig, ax = plt.subplots(4, figsize=(9,7))

    ax[0].plot(t, sine1, 'r')
    ax[0].set_title(f'Sine (fs={fs})/2 Hz')

    ax[1].plot(t, sine2, 'g')
    ax[1].set_title(f'Sine (fs={fs})/4 Hz')

    ax[2].plot(t, sine3, 'b')
    ax[2].set_title(f'Sine 0hz (constant)')

    ax[3].plot(t, sine1, 'r')
    ax[3].plot(t, sine2, 'g')
    ax[3].plot(t, sine3, 'b')
    ax[3].set_title('Overlapped: ')


    
    plt.tight_layout()
    plt.savefig("./img/6.svg")
    plt.show()