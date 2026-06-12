import streamlit as st
import cv2
import numpy as np
from pathlib import Path
from PIL import Image

from modules.filters import apply_filter, FILTER_DESCRIPTIONS
from modules.histogram import create_histogram
from modules.metrics import calculate_psnr, calculate_mse
from modules.utils import read_uploaded_image, convert_bgr_to_rgb, encode_image_png

APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR / "assets"
IMAGES_DIR = APP_DIR / "images"

st.set_page_config(
    page_title="CCTV Vision Enhancer",
    page_icon=str(ASSETS_DIR / "favicon.png"),
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f8fafc;
    }
    .block-container {
        padding-top: 1.5rem;
    }
    .metric-card {
        padding: 18px;
        border-radius: 14px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

logo_path = ASSETS_DIR / "logo.png"
banner_path = ASSETS_DIR / "banner.png"

if logo_path.exists():
    st.image(str(logo_path), width=260)

if banner_path.exists():
    st.image(str(banner_path), use_container_width=True)

st.title("📷 CCTV Vision Enhancer")
st.write(
    "Sistem peningkatan kualitas foto CCTV yang mengandung noise menggunakan "
    "Python, OpenCV, dan Streamlit."
)

st.sidebar.title("⚙️ Pengaturan")
source_type = st.sidebar.radio(
    "Pilih sumber gambar",
    ["Upload Gambar", "Gunakan Sample CCTV"]
)

filter_method = st.sidebar.selectbox(
    "Pilih metode denoising",
    list(FILTER_DESCRIPTIONS.keys())

)
st.sidebar.header("Parameter Kualitas")

quality = st.sidebar.select_slider(
    "Preset Kualitas",
    options=[
        "Low",
        "Medium",
        "High",
        "Ultra"
    ],
    value="High"
)

if quality == "Low":
    filter_strength = 5
elif quality == "Medium":
    filter_strength = 10
elif quality == "High":
    filter_strength = 15
else:
    filter_strength = 20

kernel_size = st.sidebar.slider(
    "Kernel Size",
    min_value=3,
    max_value=15,
    step=2,
    value=5
)

brightness = st.sidebar.slider(
    "Brightness",
    -100,
    100,
    0
)

contrast = st.sidebar.slider(
    "Contrast",
    0.5,
    3.0,
    1.0
)

st.sidebar.info(FILTER_DESCRIPTIONS[filter_method])

image = None
file_name = "hasil_denoise_cctv.png"

if source_type == "Upload Gambar":
    uploaded_file = st.file_uploader(
        "Upload gambar CCTV",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = read_uploaded_image(uploaded_file)
        file_name = f"hasil_{Path(uploaded_file.name).stem}.png"

else:
    sample_files = sorted(IMAGES_DIR.glob("*.jpg"))
    sample_names = [file.name for file in sample_files]

    if sample_files:
        selected_sample = st.selectbox("Pilih sample gambar CCTV", sample_names)
        selected_path = IMAGES_DIR / selected_sample
        image = cv2.imread(str(selected_path))
        file_name = f"hasil_{Path(selected_sample).stem}.png"
    else:
        st.warning("Folder images belum memiliki sample gambar.")

if image is not None:
    processed = apply_filter(
    image,
    filter_method,
    filter_strength,
    kernel_size
)
    processed = cv2.convertScaleAbs(
    processed,
    alpha=contrast,
    beta=brightness
)

    tab1, tab2, tab3 = st.tabs(
        ["🖼️ Hasil Gambar", "📊 Histogram", "📈 Analisis Kualitas"]
    )

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Gambar Asli")
            st.image(convert_bgr_to_rgb(image), use_container_width=True)

        with col2:
            st.subheader("Gambar Setelah Denoising")
            st.image(convert_bgr_to_rgb(processed), use_container_width=True)

        png_data = encode_image_png(processed)

        st.download_button(
            label="⬇️ Download Hasil Gambar",
            data=png_data,
            file_name=file_name,
            mime="image/png"
        )

    with tab2:
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Histogram Gambar Asli")
            st.pyplot(create_histogram(image))

        with col4:
            st.subheader("Histogram Gambar Hasil")
            st.pyplot(create_histogram(processed))

    with tab3:
        mse = calculate_mse(image, processed)
        psnr = calculate_psnr(image, processed)

        col5, col6, col7 = st.columns(3)
        col5.metric(
        "Metode Filter",
        filter_method
)

        col6.metric(
        "Preset",
        quality
)

        col7.metric(
        "PSNR",
        f"{psnr:.2f} dB"
)

        st.markdown(
            """
            **Keterangan singkat:**

            - MSE menunjukkan rata-rata selisih pixel antara gambar asli dan hasil proses.
            - PSNR digunakan sebagai indikator kualitas hasil pengolahan citra.
            - Semakin tinggi nilai PSNR maka kualitas gambar semakin baik.
            """
        )

else:
    st.info("Silakan upload gambar CCTV atau gunakan sample yang tersedia.")

st.markdown("---")
st.caption("© 2026 CCTV Vision Enhancer - Image Denoising System")