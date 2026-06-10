import cv2

FILTER_DESCRIPTIONS = {
    "Gaussian Blur": "Menghaluskan gambar dan mengurangi noise ringan, tetapi dapat membuat edge sedikit blur.",
    "Median Filter": "Efektif untuk mengurangi salt-and-pepper noise pada gambar CCTV.",
    "Bilateral Filter": "Mengurangi noise sambil tetap mempertahankan tepi objek agar tidak terlalu blur.",
    "Non-Local Means": "Metode denoising OpenCV yang lebih kuat untuk berbagai jenis noise.",
    "Smoothing": "Filter sederhana untuk meratakan pixel di area sekitar."
}

def apply_filter(image, method):
    if method == "Gaussian Blur":
        return cv2.GaussianBlur(image, (5, 5), 0)

    if method == "Median Filter":
        return cv2.medianBlur(image, 5)

    if method == "Bilateral Filter":
        return cv2.bilateralFilter(image, 9, 75, 75)

    if method == "Non-Local Means":
        return cv2.fastNlMeansDenoisingColored(
            image,
            None,
            10,
            10,
            7,
            21
        )

    if method == "Smoothing":
        return cv2.blur(image, (5, 5))

    return image
