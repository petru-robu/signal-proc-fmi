import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, figsize = (12, 8))

def rect_window(ws):
    return np.ones(ws)

def hanning_window(ws):
    n = np.arange(0, ws, 1)
    hanning = 0.5 * (1 - np.cos(2 * np.pi * n / ws))
    return hanning


if __name__ == '__main__':
    freq = 4
    fs = 100
    t = np.arange(0, 2, 1/fs)
    x = np.sin(2 * np.pi * freq * t)
    
    ax[0, 0].set_title(f'Sinusoida cu freq={freq}')
    ax[0, 0].plot(t, x, color='magenta')
    ax[0, 0].grid(True)
    
    ws = fs*2
    ax[0, 1].set_title(f'Diferite tipuri de ferestre')
    ax[0, 1].plot(np.arange(0, ws), rect_window(ws), color='black', label='Rect window')
    ax[0, 1].plot(np.arange(0, ws), hanning_window(ws), color='orange', label="Hanning window")
    ax[0, 1].legend()
    ax[0, 1].grid(True)
    
    ax[1, 0].set_title('Semnalul trecut prin rect')
    ax[1, 0].plot(t, x * rect_window(ws), color='k')
    ax[1, 0].grid(True)
    
    ax[1, 1].set_title('Semnalul trecut prin Hanning')
    ax[1, 1].plot(t, x * hanning_window(ws), color='orange')
    ax[1, 1].grid(True)
    
    
    
    fig.tight_layout()
    plt.savefig('./img/5.svg')
    plt.show()