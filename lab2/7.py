import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fs = 1000       
    f = 50          
    t = np.linspace(0, 0.025, fs, endpoint=False)

    sine = np.sin(2 * np.pi * f * t)

    decim_factor = 16
    sine_dec = sine[::decim_factor]
    t_dec = t[::decim_factor]

    sine_dec1 = sine[1::decim_factor]
    t_dec1 = t[1::decim_factor]

    sine_dec2 = sine[2::decim_factor]
    t_dec2 = t[2::decim_factor]

    sine_dec3 = sine[3::decim_factor]
    t_dec3 = t[3::decim_factor]

    fig, ax = plt.subplots(2, figsize=(10,7))

    ax[0].plot(t, sine, 'r')
    ax[0].set_title(f"Semnal original (fs = {fs} Hz)")

    ax[1].stem(t_dec, sine_dec, basefmt = 'b', linefmt ='r--', markerfmt = 'o')
    ax[1].stem(t_dec1, sine_dec1, basefmt = 'b', linefmt ='y--', markerfmt = ' ')
    ax[1].stem(t_dec2, sine_dec2, basefmt = 'b', linefmt ='g--', markerfmt = ' ')
    ax[1].stem(t_dec3, sine_dec3, basefmt = 'b', linefmt ='k--', markerfmt = ' ')
    ax[1].set_title(f"Semnal decimat (fs = {fs}/{decim_factor}Hz)")



    plt.tight_layout()
    plt.savefig("./img/7.svg")
    plt.show()
