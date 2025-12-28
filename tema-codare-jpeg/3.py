import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from jpeg_color import JPEGColor

def encode_to_target_mse(original_image, target_mse, max_iter=20, tol=0.01):
    scale_low, scale_high = 0.1, 10.0
    best_encoded = None
    best_scale = None
    final_mse = None

    for _ in range(max_iter):
        scale = (scale_low + scale_high) / 2
        jpeg = JPEGColor(original_image)
        jpeg.Q_matrix = jpeg.Q_matrix * scale
        encoded_image = jpeg.encode()

        mse = np.mean((original_image.astype(np.float32) - encoded_image.astype(np.float32)) ** 2)
        
        if abs(mse - target_mse) <= tol:
            best_encoded = encoded_image
            best_scale = scale
            final_mse = mse
            break
        elif mse < target_mse:
            scale_low = scale
        else:
            scale_high = scale

        best_encoded = encoded_image
        best_scale = scale
        final_mse = mse

    return best_encoded, best_scale, final_mse

if __name__ == "__main__":
    img = Image.open("./res/1.jpg").convert("RGB")
    X = np.array(img)

    print("Binary searching scale factor...")
    
    target_mse = 55
    compressed, scale, mse = encode_to_target_mse(X, target_mse)
    
    if compressed is None:
        raise ValueError('Could not achieve MSE')
    
    print("Scale factor: ", scale)
    print("MSE:", mse)

    # imaginea intreaga
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(X[345:445, 275:325])
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(compressed[345:445, 275:325])
    plt.title("JPEG")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(np.abs(X - compressed)[345:445, 275:325])
    plt.title("Diferenta")
    plt.tight_layout()
    plt.savefig("./plots/target_mse_image.svg")
    
    plt.show()