import scipy
import numpy as np
import matplotlib.pyplot as plt

no_conv = 4
fig, ax = plt.subplots(no_conv, figsize = (10, 10))

if __name__ == '__main__':
    N = 100
    
    x = np.random.random(N)
    for i in range(no_conv):
        ax[i].set_title(f"After {i} convolution/s.")
        ax[i].plot(np.arange(0, len(x)), x, color='orange')
        x = scipy.signal.convolve(x, x)
    
    fig.tight_layout()
    plt.savefig('./img/2.svg')
    plt.show()
    
    
    