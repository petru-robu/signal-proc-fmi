import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import scipy
 
fig, ax = plt.subplots(3, figsize=(10, 9))

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
    
    orders = [3, 7, 9]
    
    # Plot buttersworth for different orders
    ax[0].set_xlabel("Esantioane")
    ax[0].set_ylabel("Nr masini")
    ax[0].set_title(f"Butterworth comparison for different orders")
    ax[0].plot(t, x, label="Original", alpha=0.5)
    for order in orders:
        b, a = scipy.signal.butter(order, f_norm, btype='low')
        filtered_signal = scipy.signal.filtfilt(b, a, x)

        ax[0].plot(t, filtered_signal, label=f"Filtrat ordin={order}")
    ax[0].legend()   
    
    # Plot Chebyshev for different orders
    ax[1].set_xlabel("Esantioane")
    ax[1].set_ylabel("Nr masini")
    ax[1].set_title(f"Chebyshev comparison for different orders")
    ax[1].plot(t, x, label="Original", alpha=0.5)
    for order in orders:
        rp = 5 # atenuare <db>
        b, a = scipy.signal.cheby1(order, rp, f_norm, btype='low')
        filtered_signal = scipy.signal.filtfilt(b, a, x)

        ax[1].plot(t, filtered_signal, label=f"Filtrat ordin={order}")
    ax[1].legend()   
    
    # Plot Chebyshev for different rps
    rps = [2, 5, 10, 12]
    ax[2].set_xlabel("Esantioane")
    ax[2].set_ylabel("Nr masini")
    ax[2].set_title(f"Chebyshev comparison for different rps")
    ax[2].plot(t, x, label="Original", alpha=0.5)
    for rp in rps:
        order = 4
        b, a = scipy.signal.cheby1(order, rp, f_norm, btype='low')
        filtered_signal = scipy.signal.filtfilt(b, a, x)
        ax[2].plot(t, filtered_signal, label=f"Atenuare = {rp} dB")
        
    ax[2].legend()   
    
    
    fig.tight_layout()
    plt.savefig('img/6c.svg')
    plt.show()
