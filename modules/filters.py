import cv2

FILTER_DESCRIPTIONS = {
    "Gaussian Blur": "Menghaluskan gambar dan mengurangi noise ringan.",
    "Median Filter": "Efektif untuk mengurangi salt-and-pepper noise.",
    "Bilateral Filter": "Mengurangi noise tanpa menghilangkan edge.",
    "Non-Local Means": "Metode denoising OpenCV yang lebih kuat.",
    "Smoothing": "Filter sederhana untuk meratakan pixel."
}

def apply_filter(image, method, filter_strength=10, kernel_size=5):
    if method == "Gaussian Blur":
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    if method == "Median Filter":
        return cv2.medianBlur(image, kernel_size)

    if method == "Bilateral Filter":
        return cv2.bilateralFilter(
            image,
            kernel_size,
            filter_strength * 10,
            filter_strength * 10
        )

    if method == "Non-Local Means":
        return cv2.fastNlMeansDenoisingColored(
            image,
            None,
            filter_strength,
            filter_strength,
            7,
            21
        )

    if method == "Smoothing":
        return cv2.blur(image, (kernel_size, kernel_size))

    return image