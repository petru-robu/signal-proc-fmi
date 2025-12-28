import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from jpeg_color import JPEGColor

if __name__ == "__main__":
    # test image
    img = Image.open("./res/1.jpg").convert("RGB")
    X = np.array(img)
    jpeg = JPEGColor(X)

    X_jpeg = jpeg.encode()

    # imaginea intreaga
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(X)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(X_jpeg)
    plt.title("JPEG")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(X - X_jpeg)
    plt.title("Diferenta")
    plt.tight_layout()
    plt.savefig("./plots/endcoded_color.svg")

    # portiune 50x50
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(X[375:425, 275:325])
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(X_jpeg[375:425, 275:325])
    plt.title("JPEG")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(abs(X - X_jpeg)[375:425, 275:325])
    plt.title("Diferenta")
    plt.tight_layout()
    plt.savefig("./plots/endcoded_color_zoomed.svg")

    plt.show()
