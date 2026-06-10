import numpy as np

def calculate_mse(original, processed):
    original = original.astype("float")
    processed = processed.astype("float")
    mse = np.mean((original - processed) ** 2)
    return mse

def calculate_psnr(original, processed):
    mse = calculate_mse(original, processed)

    if mse == 0:
        return 100.0

    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr
