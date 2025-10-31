import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    freq = 220
    phi1, phi2, phi3, phi4 = np.pi/2, np.pi/3, 3*np.pi/4, 7*np.pi/6

    t = np.linspace(0, 0.025, 1000)
    s1 = np.sin(2 * np.pi * freq * t + phi1)
    s2 = np.sin(2 * np.pi * freq * t + phi2)
    s3 = np.sin(2 * np.pi * freq * t + phi3)
    s4 = np.sin(2 * np.pi * freq * t + phi4)

    fig, ax = plt.subplots(5, 2, figsize=(12, 10))

    ax[0, 0].plot(t, s1, 'r')
    ax[0, 0].plot(t, s2, 'g')
    ax[0, 0].plot(t, s3, 'b')
    ax[0, 0].plot(t, s4, 'y')
    ax[0, 0].title.set_text('220Hz sine waves with different phases')

    ax[0, 1].plot(t, s1, 'r')
    ax[0, 1].title.set_text('Clean sine 220hz, phi=pi/2')

    samples = 1000
    norm_dist = np.random.normal(size=samples)

    z_norm = np.linalg.norm(norm_dist)
    x_norm = np.linalg.norm(s1)
    idx = 1
    for ratio in [0.1, 1, 10, 100]:
        gamma = x_norm ** 2 / z_norm ** 2 / ratio
        noise = gamma * norm_dist

        ax[idx, 0].plot(t, noise)
        ax[idx, 0].title.set_text(f'Noise for SNR={ratio}')

        ax[idx, 1].plot(t, s1 + noise) 
        ax[idx, 1].title.set_text(f'220hz sine + noise; SNR={ratio}')
        idx += 1

    fig.tight_layout()
    plt.savefig("./img/2.svg")
    plt.show()
