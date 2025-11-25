import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, figsize = (10, 10))

if __name__ == '__main__':
    # esantioane
    N = 20
    ts = np.linspace(0.05, 2.05, 1000)
    xs = np.log(ts)
    t = np.linspace(0.05, 2.05, N)
    x = np.log(t)
    
    # shiftare circulara
    d = 8
    y = np.roll(x, d)
    #print(x, y)
    
    # a doua formula
    rec = np.fft.ifft(np.conjugate(np.fft.fft(y) / np.fft.fft(x)))
    shift = np.argmax(np.abs(rec)) # valoarea maxima
    print("Recovered shift:", shift) # shiftarea la dreapta
    
    # prima formula
    rec = np.fft.ifft(np.conjugate(np.fft.fft(x)) * np.fft.fft(y))
    #print(rec)
    shift = np.argmax(np.abs(rec)) # valoarea maxima
    print("Recovered shift:", shift) # shiftarea la stanga
    
    ax[0].set_title('Functia esantionata')   
    ax[0].plot(ts, xs, color='blue', label='functia log')
    ax[0].stem(t, x, linefmt='k--', basefmt='b--', label='esantioane')
    ax[0].stem(t, y, linefmt='p--', basefmt='b--', label='esantioane deplasate')
    ax[0].legend()
    ax[0].grid(True)
    
    ax[1].set_title('Rec')
    ax[1].plot(np.arange(0, len(rec)), rec, color='magenta', label='reconstructie')
    ax[1].legend()
    ax[1].grid(True)
    ax[1].set_xticks(range(len(rec)))
    
    fig.tight_layout()
    plt.savefig('./img/4.svg')
    plt.show()
    