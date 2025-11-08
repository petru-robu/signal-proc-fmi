import numpy as np
import matplotlib.pyplot as plt
import time

def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    return X

def my_fft(x):
    N = len(x)  
    if N == 1:
        return x
    X_even = my_fft(x[::2])
    X_odd = my_fft(x[1::2])    
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([X_even + factor[: N//2] * X_odd,
                            X_even + factor[N//2:] * X_odd])

def my_fft_optimized(x):
    N = len(x)  
    if N <= 32:
        return dft(x)

    X_even = my_fft(x[::2])
    X_odd = my_fft(x[1::2])    
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([X_even + factor[: N//2] * X_odd,
                            X_even + factor[N//2:] * X_odd])


def init_signal(samples=200, duration=0.1, comp=[20, 70, 100]):
    fs = samples/duration
    t = np.linspace(0, duration, samples)
    signal = np.zeros(samples)
    for fr in comp:
        signal += np.sin(2 * np.pi * 20 * t)
        
    return signal

def time_npfft(x):
    samples = len(x)
    fft_t0 = time.time()
    fft = np.fft.fft(x)
    fft_t1 = time.time()
    return fft_t1 - fft_t0

def time_fft(x):
    samples = len(x)
    fft_t0 = time.time()
    fft = my_fft(x)
    fft_t1 = time.time()
    return fft_t1 - fft_t0

def time_dft(x):
    samples = len(x)
    my_ft_t0 = time.time()
    my_ft = dft(signal)
    my_ft_t1 = time.time()
    return my_ft_t1 - my_ft_t0

def time_my_fft_o(x):
    samples = len(x)
    my_ft_o_t0 = time.time()
    my_ft = my_fft_optimized(signal)
    my_ft_o_t1 = time.time()
    return my_ft_o_t1 - my_ft_o_t0

if __name__ == '__main__':
    vals = [128, 256, 512, 1024, 2048, 4096, 8192] 

    npfft_times, dft_times, fft_times, fft_o_times = [], [], [], []
    for N in vals:
        signal = init_signal(N)
        t_npfft = time_npfft(signal)
        t_dft = time_dft(signal)
        t_fft = time_fft(signal)
        o_fft = time_my_fft_o(signal)

        print(f'N = {N} | np.fft = {t_npfft} | fft = {t_fft} | dft = {t_dft}')
        
        npfft_times.append(t_npfft)
        dft_times.append(t_dft)
        fft_times.append(t_fft)
        fft_o_times.append(o_fft)

    plt.figure(figsize=(8, 6))
    plt.title('Comparing speed between np.fft, my FFT, my FFT_O and my DFT')
    plt.grid(True)
    plt.plot(vals, np.log(npfft_times), 'r')
    plt.plot(vals, np.log(dft_times), 'b')
    plt.plot(vals, np.log(fft_times), 'y')
    plt.plot(vals, np.log(fft_o_times), 'purple')
    plt.legend(['np.fft', 'dft', 'my_fft', 'my_fft_o'])
    
    plt.tight_layout()
    plt.savefig('./img/1.svg')
    plt.show()
