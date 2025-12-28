import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    N = 200
    n1 = np.linspace(0, 1, N)
    n2 = np.linspace(0, 1, N)
    n2_grid, n1_grid = np.meshgrid(n1, n2, indexing='ij')
    
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    x1 = np.sin(2*np.pi*n1_grid + 3*np.pi*n2_grid)
    ax[0].imshow(x1, cmap='inferno', origin='lower')
    ax[0].set_title('$x_{n_1,n_2} = \\sin(2\\pi n_1 + 3\\pi n_2)$')
    spectrum1 = 20 * np.log10(abs(np.fft.fftshift(np.fft.fft2(x1))) + 1e-12)
    ax[1].imshow(spectrum1, cmap='inferno', origin='lower')
    ax[1].set_title('Spectru')
    plt.tight_layout()
    plt.savefig('img/1.svg')
    plt.close(fig)

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    x2 = np.sin(4*np.pi*n1_grid) + np.cos(3*np.pi*n2_grid)
    ax[0].imshow(x2, cmap='inferno', origin='lower')
    ax[0].set_title('$x_{n_1,n_2} = \\sin(4\\pi n_1) + \\cos(3\\pi n_2)$')
    spectrum2 = 20 * np.log10(abs(np.fft.fftshift(np.fft.fft2(x2))) + 1e-12)
    ax[1].imshow(spectrum2, cmap='inferno', origin='lower')
    ax[1].set_title('Spectru')
    plt.tight_layout()
    plt.savefig('img/2.svg')
    plt.close(fig)

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    x3 = np.zeros((N, N))
    x3[0][5] = x3[0][N-5] = 1
    x3s = np.fft.fftshift(x3)
    ax[0].imshow(x3s, cmap='inferno', origin='lower')
    ax[0].set_title('$Y_{0,5} = Y_{0,N-5} = 1$')
    spectrum3 = 20 * np.log10(abs(np.fft.fftshift(np.fft.fft2(x3s))) + 1e-12)
    ax[1].imshow(spectrum3, cmap='inferno', origin='lower')
    ax[1].set_title('Spectru')
    plt.tight_layout()
    plt.savefig('img/3.svg')
    plt.close(fig)


    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    x4 = np.zeros((N, N))
    x4[5][0] = x4[N-5][0] = 1
    x4s = np.fft.fftshift(x4)
    ax[0].imshow(x4s, cmap='inferno', origin='lower')
    ax[0].set_title('$Y_{5,0} = Y_{N-5,0} = 1$')
    spectrum4 = 20 * np.log10(abs(np.fft.fftshift(np.fft.fft2(x4s))) + 1e-12)
    ax[1].imshow(spectrum4, cmap='inferno', origin='lower')
    ax[1].set_title('Spectru')
    plt.tight_layout()
    plt.savefig('img/4.svg')
    plt.close(fig)


    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    x5 = np.zeros((N, N))
    x5[5][5] = x5[N-5][N-5] = 1
    x5s = np.fft.fftshift(x5)
    ax[0].imshow(x5s, cmap='inferno', origin='lower')
    ax[0].set_title('$Y_{5,5} = Y_{N-5,N-5} = 1$')
    spectrum5 = 20 * np.log10(abs(np.fft.fftshift(np.fft.fft2(x5s))) + 1e-12)
    ax[1].imshow(spectrum5, cmap='inferno', origin='lower')
    ax[1].set_title('Spectru')
    plt.tight_layout()
    plt.savefig('img/5.svg')
    plt.close(fig)
