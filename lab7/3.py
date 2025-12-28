import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets

X = datasets.face(gray=True)

plt.title("Imaginea originala:")
plt.imshow(X, cmap='gray')
plt.tight_layout()
plt.savefig('img/ex2-orig.svg')

# FFT
Y = np.fft.fft2(X)
Y_shift = np.fft.fftshift(Y)
mag = np.abs(Y_shift)

snr_threshold = 0.0025 * mag.max()
Y_filt = Y_shift * (mag >= snr_threshold)

# reconstrucție
Y_filt = np.fft.ifftshift(Y_filt)
X_filt = np.real(np.fft.ifft2(Y_filt))

plt.title("Imaginea comprimata:")
plt.imshow(X_filt, cmap='gray')
plt.tight_layout()
plt.savefig('img/ex3.svg')
plt.show()
plt.close()
