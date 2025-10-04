# VK-Pixel-Extraction_Rotation_Image-Mirroring

Aplikasi GUI berbasis Python untuk ekstraksi intensitas piksel gambar dan transformasi gambar (rotasi dan pencerminan). Aplikasi ini memungkinkan pengguna untuk memuat gambar, menganalisis nilai intensitas piksel RGB, serta melakukan berbagai transformasi gambar.

## 🚀 Fitur Utama

### 📊 Ekstraksi Intensitas Piksel

-   **Analisis Nilai RGB**: Ekstraksi nilai intensitas piksel Red, Green, Blue dari setiap posisi pada gambar
-   **Export ke Excel**: Menyimpan data intensitas piksel dalam format Excel (.xlsx)
-   **Visualisasi Data**: Menampilkan data intensitas piksel dalam tabel interaktif

### 🔄 Transformasi Gambar

-   **Rotasi 90° Searah Jarum Jam**: Memutar gambar 90 derajat ke kanan
-   **Rotasi 90° Berlawanan Arah Jarum Jam**: Memutar gambar 90 derajat ke kiri
-   **Pencerminan Horizontal**: Membalik gambar secara horizontal (kiri-kanan)
-   **Pencerminan Vertikal**: Membalik gambar secara vertikal (atas-bawah)

## 🛠️ Teknologi yang Digunakan

-   **Python 3.x**
-   **Tkinter**: Untuk antarmuka pengguna GUI
-   **OpenCV (cv2)**: Untuk pemrosesan gambar
-   **PIL (Python Imaging Library)**: Untuk manipulasi gambar
-   **NumPy**: Untuk operasi array dan matriks
-   **Pandas**: Untuk manipulasi data dan export Excel

## 📋 Persyaratan Sistem

### Dependencies

```bash
pip install opencv-python
pip install pillow
pip install numpy
pip install pandas
pip install openpyxl
```

### Sistem Operasi

-   Windows
-   macOS
-   Linux

### Format Gambar yang Didukung

-   JPEG (.jpg, .jpeg)
-   PNG (.png)
-   BMP (.bmp)

## 🚀 Instalasi dan Penggunaan

### 1. Clone Repository

```bash
git clone https://github.com/rai-pramana/VK-Pixel-Extraction_Rotation_Image-Mirroring.git
cd VK-Pixel-Extraction_Rotation_Image-Mirroring
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi

```bash
python pixel_extraction-rotation-image_mirroring.py
```

## 📖 Cara Penggunaan

### Memuat Gambar

1. Klik tombol **"Load Image"**
2. Pilih file gambar yang ingin diproses
3. Gambar akan ditampilkan di panel "Gambar Awal"

### Ekstraksi Intensitas Piksel

1. Setelah memuat gambar, klik **"Process Image"**
2. Data intensitas piksel akan ditampilkan dalam tab **"Intensity"**
3. Data berisi informasi posisi piksel f(x,y) dan nilai RGB

### Transformasi Gambar

1. Buka tab **"Transform"**
2. Pilih jenis transformasi yang diinginkan:
    - **Rotate 90° Clockwise**: Rotasi searah jarum jam
    - **Rotate 90° Counter Clockwise**: Rotasi berlawanan arah jarum jam
    - **Mirror Horizontal**: Pencerminan horizontal
    - **Mirror Vertical**: Pencerminan vertikal
3. Hasil transformasi akan ditampilkan di panel "Gambar Hasil"

### Menyimpan Hasil

-   **Save Gambar**: Menyimpan gambar hasil transformasi
-   **Save Pixel**: Menyimpan data intensitas piksel hasil transformasi ke Excel

## 📁 Struktur Project

```
VK-Pixel-Extraction_Rotation_Image-Mirroring/
│
├── pixel_extraction-rotation-image_mirroring.py    # File utama aplikasi
├── README.md                                       # Dokumentasi project
│
└── Hasil/                                         # Folder output hasil
    ├── intensitas_piksel_asli.xlsx               # Data piksel gambar asli
    ├── pencerminan_horizontal.png                # Hasil pencerminan horizontal
    ├── pencerminan_horizontal.xlsx               # Data piksel pencerminan horizontal
    ├── pencerminan_vertikal.png                  # Hasil pencerminan vertikal
    ├── pencerminan_vertikal.xlsx                 # Data piksel pencerminan vertikal
    ├── rotasi_90_derajat_berlawanan_arah_jarum_jam.png  # Hasil rotasi CCW
    ├── rotasi_90_derajat_berlawanan_arah_jarum_jam.xlsx # Data piksel rotasi CCW
    ├── rotasi_90_derajat_searah_jarum_jam.png    # Hasil rotasi CW
    └── rotasi_90_derajat_searah_jarum_jam.xlsx   # Data piksel rotasi CW
```

## 🔧 Fitur Aplikasi

### Interface Utama

-   **Panel Gambar Awal**: Menampilkan gambar yang dimuat
-   **Tab Intensity**: Menampilkan data intensitas piksel dalam format tabel
-   **Tab Transform**: Menyediakan opsi transformasi gambar dan menampilkan hasil

### Kontrol Aplikasi

-   **Load Image**: Memuat gambar dari file
-   **Process Image**: Menganalisis intensitas piksel
-   **Reset**: Mereset aplikasi ke kondisi awal
-   **Exit**: Keluar dari aplikasi

## 🎯 Algoritma Transformasi

### Rotasi 90° Searah Jarum Jam

```python
def rotasi_90_derajat_jarum_jam(image):
    baris, kolom, _ = image.shape
    matriks_rotasi = np.zeros((kolom, baris, image.shape[2]), dtype=image.dtype)
    for i in range(baris):
        for j in range(kolom):
            matriks_rotasi[j, baris-1-i] = image[i, j]
    return matriks_rotasi
```

### Pencerminan Horizontal

```python
def pencerminan_horizontal(image):
    baris, kolom, _ = image.shape
    matriks_pencerminan = np.zeros((baris, kolom, image.shape[2]), dtype=image.dtype)
    for i in range(baris):
        for j in range(kolom):
            matriks_pencerminan[i, kolom-1-j] = image[i, j]
    return matriks_pencerminan
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 Lisensi

Project ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.

## 👨‍💻 Pengembang

**Rai Pramana**

-   GitHub: [@rai-pramana](https://github.com/rai-pramana)

## 📞 Kontak

Jika ada pertanyaan atau saran, silakan hubungi melalui:

-   GitHub Issues: [https://github.com/rai-pramana/VK-Pixel-Extraction_Rotation_Image-Mirroring/issues](https://github.com/rai-pramana/VK-Pixel-Extraction_Rotation_Image-Mirroring/issues)

---

⭐ **Jangan lupa berikan star jika project ini bermanfaat!**
