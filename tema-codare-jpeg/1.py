import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
from jpeg import JPEG

if __name__ == "__main__":
    # test image
    X = misc.ascent()

    jpeg = JPEG(X)
    X_jpeg = jpeg.encode()

    # imaginea intreaga
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(X, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(X_jpeg, cmap="gray")
    plt.title("JPEG")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(np.abs(X - X_jpeg))
    plt.title("Diferenta")

    plt.tight_layout()
    plt.savefig("./plots/encoded_grayscale.svg")

    # zoom-in
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(X[:50, :50], cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(X_jpeg[:50, :50], cmap="gray")
    plt.title("JPEG")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(np.abs(X - X_jpeg)[375:425, 275:325])
    plt.title("Diferenta")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("./plots/encoded_grayscale_zoomed.svg")