# CCTV Vision Enhancer

Project Streamlit untuk peningkatan kualitas foto CCTV yang mengandung noise menggunakan Python dan OpenCV.

## Fitur

- Upload gambar CCTV
- Sample gambar CCTV bawaan
- Gaussian Blur
- Median Filter
- Bilateral Filter
- Non-Local Means Denoising
- Smoothing
- Perbandingan gambar asli dan hasil
- Histogram RGB sebelum dan sesudah
- Perhitungan MSE dan PSNR
- Download hasil gambar
- Logo, favicon, dan banner aplikasi

## Cara Menjalankan di VS Code

1. Extract file ZIP.
2. Buka folder project di VS Code.
3. Buka terminal di VS Code.
4. Jalankan perintah berikut:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser.

## Struktur Folder

```text
CCTV_Vision_Enhancer_Final/
├── app.py
├── requirements.txt
├── README.md
├── assets/
│   ├── logo.png
│   ├── favicon.png
│   └── banner.png
├── images/
│   ├── sample_cctv_1.jpg
│   ├── sample_cctv_2.jpg
│   └── sample_cctv_3.jpg
├── modules/
│   ├── filters.py
│   ├── histogram.py
│   ├── metrics.py
│   └── utils.py
└── outputs/
```

## Tech Stack

- Python
- OpenCV
- Streamlit
