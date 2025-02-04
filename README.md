# Pic-to-text

## Bahasa Indonesia

### Deskripsi
Pic to text adalah aplikasi sederhana berbasis **PyQt6** yang memungkinkan pengguna menempel (paste) gambar langsung ke UI, lalu mengekstrak teks menggunakan **Tesseract OCR**. Hasil OCR ditampilkan dalam bentuk teks dan dapat disimpan sebagai file **.TXT** untuk kemudahan penggunaan lebih lanjut.

### Fitur
- Paste gambar langsung dari clipboard  
- Menampilkan hasil OCR dalam tampilan teks  
- Menyimpan hasil ke format .TXT  
- Tombol reset untuk mengulang proses tanpa menutup aplikasi  
- Preprocessing gambar untuk meningkatkan akurasi OCR

<img width="752" alt="image" src="https://github.com/user-attachments/assets/2b46dec8-3728-4154-bac5-d85e288b3baa" />


### Instalasi

#### 1. Install Tesseract OCR
**Untuk macOS (Homebrew):**  

brew install tesseract

**Untuk Windows:**
1.	Download & install dari Tesseract OCR
2.	Tambahkan path pytesseract.pytesseract.tesseract_cmd di script jika diperlukan

### 2. Install dependensi Python

pip install pytesseract opencv-python numpy pandas pyqt6

### Cara Penggunaan
1.	Jalankan aplikasi

python ptt.py

2.	Paste gambar dari clipboard dengan menekan tombol Paste Image
3.	Lihat hasil OCR dalam tampilan teks di UI
4.	Simpan hasil ke .TXT menggunakan tombol Save to TXT
5.	Gunakan tombol Reset untuk mengulang dari awal tanpa menutup aplikasi

### Disclaimer

### Mengingat akurasi OCR bergantung pada kualitas gambar, hasil teks mungkin tidak selalu sesuai dengan yang diharapkan. Jika teks yang diekstrak kurang akurat, coba gunakan gambar dengan kontras tinggi dan teks yang jelas.




English

### Description

### OCR Table Extractor is a simple PyQt6-based application that allows users to paste images directly into the UI, then extract text using Tesseract OCR. The extracted text is displayed in the app and can be saved as a .TXT file for easy further use.

Features
	•	Paste images directly from clipboard
	•	Display OCR results in a text view
	•	Save results as a .TXT file
	•	Reset button to restart without closing the app
	•	Image preprocessing for better OCR accuracy


<img width="752" alt="image" src="https://github.com/user-attachments/assets/6709701a-4f3a-440e-9503-1d08d4dded22" />

 
### Installation

1. Install Tesseract OCR

**For macOS (Homebrew):**

brew install tesseract

**For Windows:**
1.	Download & install from Tesseract OCR
2.	Set pytesseract.pytesseract_cmd in the script if needed

### 2. Install Python dependencies

pip install pytesseract opencv-python numpy pandas pyqt6

### How to Use
1.	Run the application

python ptt.py

2.	Paste an image from the clipboard by clicking the Paste Image button
3.	View OCR results in the text display area
4.	Save the results as a .TXT file with the Save to TXT button
5.	Use the Reset button to start over without restarting the app

### Disclaimer

### OCR accuracy depends on image quality, and the extracted text may not always be perfect. If the OCR result is inaccurate, try using an image with high contrast and clear text.
