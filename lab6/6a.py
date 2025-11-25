import numpy as np
import matplotlib.pyplot as plt

 
fig, ax = plt.subplots(2, figsize=(10, 9))

if __name__ == '__main__':
    # Get signal data
    # 3 days = 3 * 24 = 72h
    start, N = 2075, 72
    end = start + N
    contents = np.genfromtxt('Train.csv', delimiter=',')
    t = np.arange(0, N)
    x = contents[:, 2][1:][start:end]
    
    # Plot raw signal
    ax[0].set_title("Semnalul brut pe 3 zile")
    ax[0].plot(t, x, label="semnalul brut")
    ax[0].set_xlabel('Esantioane')
    ax[0].set_ylabel('Nr masini')
    ax[0].set_xticks(range(0, N+1, 3))
    ax[0].grid(True)
    ax[0].legend()
    
    # Plot lowpass filtered signal
    ax[1].set_title("Lowpass filters")
    ax[1].plot(t, x, label="semnalul brut", color='gray', alpha=0.2, ls='dashed')
    ws_sizes = [5, 9, 13, 17]
    for ws in ws_sizes:
        lp = np.convolve(x, np.ones(ws), 'valid') / ws
        ax[1].plot(t[ws-1:], lp, label=f'ws={ws}')
    ax[1].legend()
        
    fig.tight_layout()
    plt.savefig('img/6a.svg')
    plt.show()
