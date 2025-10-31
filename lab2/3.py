import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy

if __name__ == '__main__':
    duration = 2
    sr = 44100
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)

    # sine wave 400Hz
    freq = 400
    a = np.sin(2 * np.pi * freq * t)

    # sine wave 800Hz
    freq = 800
    b = np.sin(2 * np.pi * freq * t)

    # sawtooth 400Hz
    freq = 400
    c = freq * t - np.floor(freq * t)

    # square 800Hz
    freq = 800
    d = 4 * np.floor(freq*t) - 2 * np.floor(2*freq*t) + 1

    signals_paths = {
        './audio/a.wav': a,
        './audio/b.wav': b,
        './audio/c.wav': c,
        './audio/d.wav': d,
    }

    # play signals
    # for s in signals_paths:
    #     sd.play(signals_paths[s], sr)
    #     sd.wait()

    # save signals
    for path in signals_paths:
        scipy.io.wavfile.write(path, sr, signals_paths[path])

    # read and plot signals
    fig, ax = plt.subplots(4, figsize=(10, 8))
    idx = 0
    for path in signals_paths:
        rate, sgn = scipy.io.wavfile.read(path)
        t = np.linspace(0, 0.001, len(sgn))
        ax[idx].plot(t[:2000], sgn[:2000])
        ax[idx].set_title(path.split('/')[-1])
        idx += 1


    fig.suptitle('Signals read from saved audio wav files', fontsize=16)
    fig.tight_layout()
    plt.savefig("./img/3.svg")
    plt.show()

