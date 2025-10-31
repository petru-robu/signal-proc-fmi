import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

if __name__ == '__main__':
    duration = 1
    sr = 20000        
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)

    # sine waves
    sine1 = np.sin(2 * np.pi * 400 * t)
    sine2 = np.sin(2 * np.pi * 800 * t)

    # concatenate
    comb_sine = np.concatenate((sine1, sine2))
    comb_t = np.linspace(0, duration * 2, int(sr * duration * 2), endpoint=False)

    fig, ax = plt.subplots(3, figsize=(10,6))

    ax[0].plot(t[:400], sine1[:400], 'r')
    ax[0].set_title('Sine 400Hz')

    ax[1].plot(t[:400], sine2[:400], 'g')
    ax[1].set_title('Sine 800Hz')

    ax[2].plot(comb_t[:800], comb_sine[:800], 'b')
    ax[2].set_title('Combined')

    sd.play(comb_sine, sr)
    sd.wait()

    fig.suptitle('Concatenated Signals', fontsize=16)
    fig.tight_layout()
    #plt.savefig("./img/5.svg")
    plt.show()
