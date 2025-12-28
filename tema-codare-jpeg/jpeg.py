import numpy as np
from scipy.fft import dctn, idctn

Q_jpeg = [
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 28, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99],
]

class JPEG:
    def __init__(self, original, Q_matrix=Q_jpeg):
        self.original = original
        self.H, self.W = self.original.shape
        self.Q_matrix = Q_matrix
        self.block_size = 8
        self.encoded_image = np.zeros_like(self.original)

    def preprocess(self):
        # completam sa avem o imagine cu dimensiune multiplu de 8
        self.padded = self.original.copy()
        pad_H = (self.block_size - self.H % self.block_size) % self.block_size
        pad_W = (self.block_size - self.W % self.block_size) % self.block_size
        if pad_H > 0 or pad_W > 0:
            self.padded = np.pad(self.padded, ((0, pad_H), (0, pad_W)), mode="constant")

        # centram valorile pixelilor in 0
        self.padded -= 128

    def process_block(self, block):
        # DCT si cuantizare
        y = np.array(dctn(block, type=2, norm="ortho"))
        yq = self.Q_matrix * np.round(y / self.Q_matrix)

        # reconstruire
        block_rec = np.array(idctn(yq, type=2, norm="ortho"))
        block_rec += 128
        block_rec = np.clip(block_rec, 0, 255)
        return block_rec

    def encode(self):
        self.preprocess()
        H_pad, W_pad = self.padded.shape
        encoded = np.zeros_like(self.padded)

        for i in range(0, H_pad, self.block_size):
            for j in range(0, W_pad, self.block_size):
                block = self.padded[i : i + self.block_size, j : j + self.block_size]
                encoded_block = self.process_block(block)
                encoded[i : i + self.block_size, j : j + self.block_size] = (
                    encoded_block
                )

        # revenim la dimensiunea originala
        self.encoded_image = encoded[: self.H, : self.W]
        return self.encoded_image

