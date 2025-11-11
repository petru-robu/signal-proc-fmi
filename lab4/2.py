import numpy as np
import matplotlib.pyplot as plt

fig, at = plt.subplots(3, figsize=(12, 9))

if __name__ == '__main__':
    t = np.linspace(0, 1, 2000, endpoint=False) # nu esantionez ultimul

    fs = 7
    t_e = np.linspace(0, 1, fs, endpoint=False) # nu esantionez ultimul
 
    f = 1
    f1 = f + 1*fs
    f2 = f + 2*fs
    f3 = f + 3*fs

    plt.suptitle(f'Aliasing with fs = {fs}Hz, base freq f={f}Hz')

    at[0].plot(t, np.sin(2 * np.pi * f1 * t ), 'y')
    at[0].stem(t_e, np.sin(2 * np.pi * f1 * t_e), markerfmt='ko', linefmt='k', basefmt='k--')
    at[0].set_title(f"f1={f1} Hz")

    at[1].plot(t, np.sin(2 * np.pi * f2 * t), 'purple')
    at[1].stem(t_e, np.sin(2 * np.pi * f2 * t_e), markerfmt='ko', linefmt='k', basefmt='k--')
    at[1].set_title(f"f2={f2} Hz")

    at[2].plot(t, np.sin(2 * np.pi * f3 * t), 'green')
    at[2].stem(t_e, np.sin(2 * np.pi * f3 * t_e), markerfmt='ko', linefmt='k', basefmt='k--')
    at[2].set_title(f"f3={f3} Hz")


    fig.tight_layout()
    fig.savefig("./img/2.svg")
    plt.show()
