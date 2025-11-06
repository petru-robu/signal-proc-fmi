import numpy as np
import matplotlib.pyplot as plt
import time

fig, ax = plt.subplots(3, figsize=(12,9))

if __name__ == '__main__':
    # first sine
    f1, s1, fs1 = 1200, 1000, 2000
    T1 = 1/f1

    t1 = np.linspace(0, T1*3, s1, endpoint=False)
    sine1 = np.sin(2 * np.pi * f1 * t1)
    ax[0].plot(t1, sine1, 'y')

    # first sine with few samples
    s1_samp = 9
    t1_samp = np.linspace(0, T1*3, s1_samp, endpoint=False)
    sine1_samp = np.sin(2 * np.pi * f1 * t1_samp)
    ax[0].stem(t1_samp, sine1_samp, 'purple')

    # second sine
    f2 = f1 - 3*fs1
    # t2 = np.linspace(0, T1*3, s1, endpoint=False)
    sine2 = np.sin(2 * f2 * np.pi * t1)
    ax[1].plot(t1, sine2, 'b')
    ax[1].stem(t1_samp, sine1_samp, 'purple')


    plt.tight_layout()
    plt.savefig('./img/2.svg')
    plt.show()