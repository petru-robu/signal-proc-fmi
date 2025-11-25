import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import scipy
 
fig, ax = plt.subplots(2, figsize=(10, 9))

if __name__ == '__main__':
    # Get signal data
    # 3 days = 3 * 24 = 72h
    start, N = 2075, 72
    end = start + N
    contents = np.genfromtxt('Train.csv', delimiter=',')
    t = np.arange(0, N)
    x = contents[:, 2][1:][start:end]
    
    fs = 1 / 3600  
    fc = fs / 5  
    fn = fs / 2   
    f_norm = fc / fn  
    order = 5 
    
    b, a = scipy.signal.butter(order, f_norm, btype='low')
    filtered_signal = scipy.signal.filtfilt(b, a, x)
    
    ax[0].plot(t, x, label="Original", alpha=0.5)
    ax[0].plot(t, filtered_signal, label="filtrat", color='red')
    ax[0].set_title("Butterworth")
    ax[0].set_xlabel('Esantioane')
    ax[0].set_ylabel('Nr masini')
    ax[0].set_xticks(range(0, N+1, 3))
    ax[0].legend()
    
    rp = 5 # atenuare <db>
    b, a = scipy.signal.cheby1(order, rp, f_norm, btype='low')
    filtered_signal = scipy.signal.filtfilt(b, a, x)
    
    ax[1].plot(t, x, label="Original", alpha=0.5)
    ax[1].plot(t, filtered_signal, label="filtrat", color='red')
    ax[1].set_title("Chebyshev")
    ax[1].set_xlabel('Esantioane')
    ax[1].set_ylabel('Nr masini')
    ax[1].set_xticks(range(0, N+1, 3))
    ax[1].legend()
    
    fig.tight_layout()
    plt.savefig('img/6b.svg')
    plt.show()
