import cv2
import numpy as np

def read_uploaded_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError("File gambar tidak dapat dibaca.")

    return image

def convert_bgr_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def encode_image_png(image):
    success, buffer = cv2.imencode(".png", image)

    if not success:
        raise ValueError("Gambar gagal dikonversi ke PNG.")

    return buffer.tobytes()
