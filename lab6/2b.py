import scipy
import numpy as np
import matplotlib.pyplot as plt

no_conv = 4
fig, ax = plt.subplots(no_conv, figsize = (10, 10))

if __name__ == '__main__':
    N = 100
    # rectangular signal
    x = np.concatenate([
        np.zeros(N//3),
        np.ones(N//3),
        np.zeros(N//3)
    ])
    for i in range(no_conv):
        ax[i].set_title(f"After {i} convolution/s.")
        ax[i].plot(np.arange(0, len(x)), x, color='magenta')
        x = scipy.signal.convolve(x, x)
    
    fig.tight_layout()
    plt.savefig('./img/2b.svg')
    plt.show()
    
    
    