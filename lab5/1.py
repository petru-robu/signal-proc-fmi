import numpy as np
import matplotlib.pyplot as plt
 
fig, ax = plt.subplots(2, figsize=(10, 9))

# plot data from csv
if __name__ == '__main__':
    contents = np.genfromtxt('Train.csv', delimiter=',')
    N = len(contents)
    print(f'Nr. esantioane: {N}')
    ids = contents[:, 0]
    counts = contents[:, 2]

    ax[0].plot(ids, counts, label="semnalul brut")
    ax[0].set_xlabel('Esantioane')
    ax[0].set_ylabel('Nr masini')
    ax[0].legend()
    ns = 1000

    ws_day = 24    
    ws_week = 24*7  

    mean_day = np.convolve(counts[:ns], np.ones(ws_day)/ws_day, mode='valid')
    mean_week = np.convolve(counts[:ns], np.ones(ws_week)/ws_week, mode='valid')
    x_day = ids[:len(mean_day)]
    x_week = ids[:len(mean_week)]

    ax[1].plot(ids[:ns], counts[:ns], color='blue', label='semnalul brut')    
    ax[1].plot(x_week, mean_week, color='brown', label='saptamani')  
    ax[1].plot(x_day, mean_day, color='orange', label='zile')    
    ax[1].set_xlabel('Esantioane')
    ax[1].set_ylabel('Nr masini')
    ax[1].legend()

    fig.tight_layout()
    plt.savefig('img/1.svg')
    plt.show()
