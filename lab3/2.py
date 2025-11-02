import numpy as np
import matplotlib.pyplot as plt
from helpers import colored_line_between_pts

if __name__ == '__main__':
    samples = 1000
    freq = 10
    t = np.linspace(0, 1, samples)
    sine = np.sin(3 * freq * np.pi * t)

    fig, ax = plt.subplots(3, 2, figsize=(12, 12))

    idx = 0
    for u in [1, 2, 5, 7, 13, freq]:
        wrapping = sine * np.exp(-2j * np.pi * u * t)
        d = np.hypot(np.real(wrapping), np.imag(wrapping))

        ax[idx//2, idx%2].set_aspect('equal')
        ax[idx//2, idx%2].plot(np.real(wrapping), np.imag(wrapping))
        ax[idx//2, idx%2].set_title(f'wrapping freq = {u}')

        colored_line_between_pts(np.real(wrapping), np.imag(wrapping), d, ax[idx//2, idx%2], linewidth=1)
        idx += 1


    plt.tight_layout()
    plt.savefig('./img/2.svg')
    plt.show()