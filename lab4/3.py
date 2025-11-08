import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, figsize=(12, 9))

if __name__ == '__main__':
    f, fs = 7, 7
    t = np.linspace(0, 1, 1000, endpoint=False)
    sine = np.sin(2 * np.pi * f * t)

    N = 8
    t_e = np.arange(N) / fs
    t_e = t_e[:-1]

    #print(np.arange(N) / fs)
    sine_e = np.sin(2 * np.pi * f * t_e)

    fig.suptitle(f'Aliasing with fs={fs}Hz sampling frequency')

    ax[0].plot(t, sine, 'g')
    ax[0].stem(t_e, sine_e, markerfmt= 'go', linefmt = 'g-', basefmt='g-')
    ax[0].title.set_text(f'f = {f}Hz')

    f_al = f + fs
    sine_al = np.sin(2 * np.pi * f_al * t)
    sine_al_e = np.sin(2 * np.pi * f_al * t_e)
    ax[1].plot(t, sine_al, 'r')
    ax[1].stem(t_e, sine_e, markerfmt= 'go', linefmt = 'g-', basefmt='g-')
    ax[1].title.set_text(f'f = {f_al}Hz')

    f_al = f + 2 * fs
    sine_al = np.sin(2 * np.pi * f_al * t)
    sine_al_e = np.sin(2 * np.pi * f_al * t_e)
    ax[2].plot(t, sine_al, 'b')
    ax[2].stem(t_e, sine_e, markerfmt= 'go', linefmt = 'g-', basefmt='g-')
    ax[2].title.set_text(f'f = {f_al}Hz')

    plt.tight_layout()
    plt.savefig('./img/2.svg')
    plt.show()
