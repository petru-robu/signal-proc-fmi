import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(3, figsize=(10, 9))

if __name__ == '__main__':
    # Get signal data
    contents = np.genfromtxt('Train.csv', delimiter=',')
    ids = contents[:, 0][1:]
    counts = contents[:, 2][1:]
    N = len(ids)
    
    # Sampling rate
    dt = 3600
    fs = 1 / dt

    # Plot raw signal
    ax[0].set_title(f"Raw Signal")
    ax[0].plot(ids, counts, label="semnalul brut")
    ax[0].set_xlabel('Esantioane')
    ax[0].set_ylabel('Nr masini')
    ax[0].legend()
    
    # Filtru medie mobila
    # hintv = 10
    # lowpass = []
    # for i in range(0, len(counts)-hintv):
    #     lowpass.append(np.mean(counts[i:i+hintv]))
        
    # Vectorizat:
    hintv = 10
    kernel = np.ones(hintv) / hintv
    lowpass = np.convolve(counts, kernel, mode='valid') # convolution

    dur, start = 230, 2075
    end = start + dur
    
    ax[1].set_title(f"Filtru medie mobila ({hintv} ore) pe perioada ({start}:{end})")
    ax[1].plot(ids[start:end], counts[start:end], linestyle='--', color='gold', label="semnalul brut")
    ax[1].plot(ids[start:end], lowpass[start:end], color='r', label="semnalul filtrat")
    ax[1].set_xlabel('Esantioane')
    ax[1].set_ylabel('Nr masini')
    ax[1].legend()
    
    # Filtru Blackman
    hintv = 10
    kernel = np.blackman(hintv)
    kernel = kernel / np.sum(kernel)
    blackman= np.convolve(counts, kernel, mode='valid') #convolve
    
    ax[2].set_title(f"Filtru blackman ({hintv} h) pe perioada ({start}:{end})")
    ax[2].plot(ids[start:end], counts[start:end], linestyle='--', color='gold', label="semnalul brut")
    ax[2].plot(ids[start:end], blackman[start:end], color='r', label="semnalul filtrat")
    ax[2].set_xlabel('Esantioane')
    ax[2].set_ylabel('Nr masini')
    ax[2].legend()

    fig.tight_layout()
    plt.savefig('img/5.svg')
    plt.show()
    
