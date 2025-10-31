import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # semnal continuu
    t = np.linspace(0, 0.03, 1000)
    print(len(t))

    x = np.cos(520 * np.pi * t + np.pi / 3)
    y = np.cos(280 * np.pi * t - np.pi/3)
    z = np.cos(120 * np.pi * t + np.pi /3)

    fig, ax = plt.subplots(3)
    ax[0].plot(t, x, 'b')
    ax[1].plot(t, y, 'b')
    ax[2].plot(t, z, 'b')

    ax[0].title.set_text("Freq: 260Hz; Phase: +pi/3")
    ax[1].title.set_text("Freq: 120Hz; Phase: -pi/3")
    ax[2].title.set_text("Freq: 60hz; Phase: +pi/3")

    # esantionare
    fs = 200
    tn = np.arange(0, 0.03, 1/fs)
    xn = np.cos(520 * np.pi * tn + np.pi / 3)
    yn = np.cos(280 * np.pi * tn - np.pi / 3)
    zn = np.cos(120 * np.pi * tn + np.pi / 3)

    ax[0].stem(tn, xn, 'b')
    ax[1].stem(tn, yn, 'b')
    ax[2].stem(tn, zn, 'b')

    fig.tight_layout()
    plt.savefig("./img/1.svg")
    plt.show()
