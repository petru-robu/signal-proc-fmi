import scipy
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, figsize = (10,8))

if __name__ == '__main__':
    B = 1
    
    t = np.linspace(-3, 3, 1000)
    sinc = np.sinc(B * t) * np.sinc(B * t)
    
    idx = 0
    freqs = np.array([1, 1.5, 2, 4], float)
    
    for ax in ax.flat:
        fs = freqs[idx]
        e_t = np.arange(0, 3.001, 1/fs)
        e_t = np.concatenate([-e_t[::-1][:-1], e_t]) 
        e_sinc = np.sinc(B * e_t) * np.sinc(B * e_t)

        #print(e_t)

        ts = 1/fs
        rec = np.zeros_like(t)
        
        for n in range(len(e_t)):
            rec += e_sinc[n] * np.sinc((t - e_t[n])/ts)
        
        ax.plot(t, sinc, 'orange', label='$sinc^{2}(Bt)$')
        ax.plot(t, rec, 'g--', label='sinc reconstructed')
        ax.stem(e_t, e_sinc, basefmt = 'k', linefmt = 'k', markerfmt = 'k')
        
        ax.set_title("$F_{s}=$" + f"{fs}Hz")
        ax.grid(True)
        ax.legend()
        
        idx += 1
    
        
    fig.tight_layout()
    plt.savefig('./img/1.svg')
    plt.show()
    
    
    