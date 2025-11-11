import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, figsize=(12, 9))

if __name__ == '__main__':
    t = np.linspace(0, 1, 2000, endpoint=False) # nu esantionez ultimul

    fs_init= 7
    fs = 25
    t_e = np.linspace(0, 1, fs, endpoint=False) # nu esantionez ultimul

    f = 1
    f1 = f + 1*fs_init
    f2 = f + 2*fs_init
    f3 = f + 3*fs_init

    plt.suptitle(f'Aliasing with fs = {fs}Hz, base freq f={f}Hz')

    ax[0].plot(t, np.sin(2 * np.pi * f1 * t ), 'y')
    ax[0].stem(t_e, np.sin(2 * np.pi * f1 * t_e), markerfmt='ko', linefmt='k', basefmt='k--')
    ax[0].set_title(f"f1={f1} Hz - doesn't alias anymore")

    ax[1].plot(t, np.sin(2 * np.pi * f2 * t), 'purple')
    ax[1].stem(t_e, np.sin(2 * np.pi * f2 * t_e), markerfmt='ko', linefmt='k', basefmt='k--')
    ax[1].stem(t_e, np.sin(2 * np.pi * f1 * t_e), markerfmt='ro', linefmt='r', basefmt='r--')
    ax[1].set_title(f"f2={f2} Hz - doesn't alias anymore")

    ax[2].plot(t, np.sin(2 * np.pi * f3 * t), 'green')
    ax[2].stem(t_e, np.sin(2 * np.pi * f3 * t_e), markerfmt='ko', linefmt='k', basefmt='k--')
    ax[2].stem(t_e, np.sin(2 * np.pi * f2 * t_e), markerfmt='bo', linefmt='b', basefmt='b--')
    ax[2].stem(t_e, np.sin(2 * np.pi * f1 * t_e), markerfmt='ro', linefmt='r', basefmt='r--')
    ax[2].set_title(f"f3={f3} Hz - doesn't alias anymore")


    fig.tight_layout()
    fig.savefig("./img/3.svg")
    plt.show()
