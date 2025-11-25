import numpy as np

def naive_multip(p1, p2):
    n = len(p1)
    m = len(p2)
    ans = [0] * (n + m - 1)

    for i in range(n):
        for j in range(m):
            ans[i + j] += p1[i] * p2[j]

    return ans

def fft_multiply(p1, p2):
    n = len(p1)
    m = len(p2)
    size = n + m - 1
    
    N = 2 ** int(np.ceil(np.log2(size))) 
    
    dft_p1 = np.fft.fft(p1, N) # pad with zeros to have size N
    dft_p2 = np.fft.fft(p2, N)
    
    result = np.fft.ifft(dft_p1 * dft_p2)
    return np.abs(result)[:size].astype(int)

if __name__ == '__main__':
    N = 10
    p = np.random.randint(0, 1000, size=N)
    q = np.random.randint(0, 1000, size=N)
    
    r_naive = naive_multip(p, q)
    r_fft = fft_multiply(p, q)

    print(r_naive)
    print(r_fft)
    print('Is FFT and naive the same: ', np.allclose(r_naive, r_fft))