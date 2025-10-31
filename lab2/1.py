import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    amp = 2 
    freq = 240
    phi = np.pi/3

    t = np.linspace(0, 0.075, 1000)
    sine = amp * np.sin(2 * np.pi * freq * t + phi)
    cosine = amp * np.cos(2 * np.pi * freq * t + phi)

    fig, ax = plt.subplots(3)
    
    ax[0].plot(t, sine, 'b')
    ax[0].plot(t, cosine, 'r')
    ax[0].title.set_text('Cosine and sine amp:2; freq:240; phi:pi/3')

    ax[1].plot(t, sine, 'b')
    ax[1].title.set_text('Sine amp:2; freq:240; phi:pi/3')

    ax[2].plot(t, cosine, 'r')
    ax[2].title.set_text('Cosine amp:2; freq:240; phi:pi/3-pi/2')

    fig.suptitle('Sine and cosine and phase difference between signals', fontsize=16)
    fig.tight_layout()
    plt.savefig("./img/1.svg")
    plt.show()


    
