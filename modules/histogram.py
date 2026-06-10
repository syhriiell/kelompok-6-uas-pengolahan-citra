import cv2
import matplotlib.pyplot as plt

def create_histogram(image):
    fig, ax = plt.subplots(figsize=(7, 4))

    colors = ("b", "g", "r")
    labels = ("Blue", "Green", "Red")

    for channel, color, label in zip(range(3), colors, labels):
        hist = cv2.calcHist([image], [channel], None, [256], [0, 256])
        ax.plot(hist, color=color, label=label)

    ax.set_title("RGB Histogram")
    ax.set_xlabel("Intensitas Pixel")
    ax.set_ylabel("Jumlah Pixel")
    ax.legend()
    ax.grid(True, alpha=0.3)

    return fig
