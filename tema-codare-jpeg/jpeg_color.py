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

class JPEGColor:
    def __init__(self, original, Q_matrix=Q_jpeg):
        self.original = original.astype(np.float32)
        self.H, self.W, _ = self.original.shape
        self.Q_matrix = np.array(Q_matrix)
        self.block_size = 8
        self.encoded_image = np.zeros_like(self.original)

    def rgb_to_ycrcb(self, img):
        R, G, B = img[..., 0], img[..., 1], img[..., 2]
        Y = 0.299 * R + 0.587 * G + 0.114 * B
        Cr = (R - Y) * 0.713 + 128
        Cb = (B - Y) * 0.564 + 128
        return np.stack([Y, Cr, Cb], axis=-1)

    def ycrcb_to_rgb(self, img):
        Y, Cr, Cb = img[..., 0], img[..., 1], img[..., 2]
        R = Y + 1.403 * (Cr - 128)
        B = Y + 1.773 * (Cb - 128)
        G = (Y - 0.299 * R - 0.114 * B) / 0.587
        rgb = np.stack([R, G, B], axis=-1)
        return np.clip(rgb, 0, 255)

    def preprocess_channel(self, channel):
        # completam sa avem o imagine cu dimensiune multiplu de 8
        pad_H = (self.block_size - self.H % self.block_size) % self.block_size
        pad_W = (self.block_size - self.W % self.block_size) % self.block_size

        padded = channel.copy()
        if pad_H > 0 or pad_W > 0:
            padded = np.pad(channel, ((0, pad_H), (0, pad_W)), mode="constant")

        # centram valorile pixelilor in 0
        padded -= 128
        return np.array(padded)

    def process_block(self, block):
        y = np.array(dctn(block, type=2, norm="ortho"))
        yq = self.Q_matrix * np.round(y / self.Q_matrix)
        block_rec = np.array(idctn(yq, type=2, norm="ortho"))
        block_rec = np.round(block_rec + 128)
        return np.clip(block_rec, 0, 255)

    def encode_channel(self, channel):
        padded = self.preprocess_channel(channel)
        H_pad, W_pad = padded.shape
        encoded = np.zeros_like(padded)
        for i in range(0, H_pad, self.block_size):
            for j in range(0, W_pad, self.block_size):
                block = padded[i : i + self.block_size, j : j + self.block_size]
                encoded_block = self.process_block(block)
                encoded[i : i + self.block_size, j : j + self.block_size] = (
                    encoded_block
                )
        return encoded[: self.H, : self.W]

    def encode(self):
        ycrcb = self.rgb_to_ycrcb(self.original)

        encoded_y = self.encode_channel(ycrcb[..., 0])
        encoded_cr = self.encode_channel(ycrcb[..., 1])
        encoded_cb = self.encode_channel(ycrcb[..., 2])

        encoded_ycrcb = np.stack([encoded_y, encoded_cr, encoded_cb], axis=-1)

        self.encoded_image = self.ycrcb_to_rgb(encoded_ycrcb)
        return self.encoded_image.astype(np.uint8)
