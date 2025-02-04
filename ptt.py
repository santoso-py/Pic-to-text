import sys
import pytesseract
import pandas as pd
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                             QLabel, QFileDialog, QTextEdit, QGraphicsView, QGraphicsScene, 
                             QGraphicsPixmapItem)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import cv2
import numpy as np

# Set path Tesseract di macOS
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

class OCRApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout utama
        layout = QVBoxLayout()

        # Tombol Paste Gambar
        self.paste_button = QPushButton("Paste Image")
        self.paste_button.clicked.connect(self.paste_image)
        layout.addWidget(self.paste_button)

        # Area Tampilan Gambar (DIBESARIN)
        self.image_view = QGraphicsView()
        self.image_scene = QGraphicsScene()
        self.image_view.setScene(self.image_scene)
        self.image_view.setFixedSize(600, 400)  # Ukuran tampilan gambar diperbesar
        layout.addWidget(self.image_view)

        # Hasil OCR dalam bentuk teks
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setFixedSize(600, 400)
        layout.addWidget(self.result_text)

        # Tombol Save ke CSV revisi ke txt
        self.save_button = QPushButton("Save to TXT")
        self.save_button.clicked.connect(self.save_to_txt)
        layout.addWidget(self.save_button)

        # Tombol Reset
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_app)
        layout.addWidget(self.reset_button)

        self.setLayout(layout)
        self.setWindowTitle("OCR Table Extractor")
        self.setGeometry(100, 100, 600, 500)

        self.image = None  # Variabel buat simpan gambar

    def paste_image(self):
        clipboard = QApplication.clipboard()
        pixmap = clipboard.pixmap()

        if not pixmap.isNull():
            self.display_image(pixmap)
            self.process_ocr()

    def display_image(self, pixmap):
        """ Menampilkan gambar di UI """
        self.image_scene.clear()
        self.image = pixmap
        item = QGraphicsPixmapItem(pixmap)
        self.image_scene.addItem(item)
        self.image_view.fitInView(item, Qt.AspectRatioMode.KeepAspectRatio)

    def process_ocr(self):
        """ Jalankan OCR dan tampilkan hasilnya """
        if self.image:
            # Konversi dari QPixmap ke OpenCV format
            image_qt = self.image.toImage()
            width, height = image_qt.width(), image_qt.height()
            ptr = image_qt.bits()
            ptr.setsize(height * width * 4)  # 4 bytes per pixel (RGBA)
            arr = np.array(ptr).reshape((height, width, 4))
            gray_image = cv2.cvtColor(arr, cv2.COLOR_RGBA2GRAY)

            # Preprocessing: Thresholding dan Noise Reduction untuk meningkatkan akurasi OCR
            gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)  # Mengurangi noise
            _, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            # Jalankan OCR
            ocr_result = pytesseract.image_to_string(thresh_image, config="--psm 6")

            # Simpan hasil di text edit
            self.result_text.setPlainText(ocr_result)

    def save_to_txt(self):
        """ Simpan hasil OCR ke TXT """
        text = self.result_text.toPlainText()
        if text.strip():
            # Pilih lokasi penyimpanan
            file_path, _ = QFileDialog.getSaveFileName(self, "Save TXT", "", "Text Files (*.txt)")
            if file_path:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text)
                self.result_text.setPlainText(f"Hasil OCR telah disimpan ke {file_path}")



    def reset_app(self):
        """ Reset aplikasi tanpa restart """
        self.image_scene.clear()
        self.result_text.clear()
        self.image = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCRApp()
    window.show()
    sys.exit(app.exec())
