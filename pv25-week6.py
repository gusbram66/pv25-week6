import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class FontSliderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 6 F1D022052 Ida Bagus Brahmanta Jayana")

        self.nama = "Ida Bagus Brahmanta Jayana"   
        self.nim = "F1D022052"

        self.label = QLabel(self.nim)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 30))
        self.update_label_colors(0, 255)

        self.font_slider = self.create_slider(20, 60, 30, self.update_font_size, "Font Size")

        self.font_color_slider = self.create_slider(0, 255, 0, self.update_colors, "Font Color")

        self.bg_color_slider = self.create_slider(0, 255, 255, self.update_colors, "Background Color")

        self.nama_label = QLabel(f"Name: {self.nama} | NIM: {self.nim}")
        self.nama_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(self.font_slider['layout'])
        layout.addLayout(self.font_color_slider['layout'])
        layout.addLayout(self.bg_color_slider['layout'])
        layout.addWidget(self.nama_label)

        self.setLayout(layout)

    def create_slider(self, min_val, max_val, start_val, slot_func, label_text):
        label = QLabel(label_text)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(start_val)
        slider.valueChanged.connect(slot_func)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(slider)

        return {'slider': slider, 'layout': layout}

    def update_font_size(self, value):
        font = self.label.font()
        font.setPointSize(value)
        self.label.setFont(font)

    def update_colors(self):
        font_gray = self.font_color_slider['slider'].value()
        bg_gray = self.bg_color_slider['slider'].value()
        self.update_label_colors(font_gray, bg_gray)

    def update_label_colors(self, font_gray, bg_gray):
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, QColor(font_gray, font_gray, font_gray))
        palette.setColor(QPalette.Window, QColor(bg_gray, bg_gray, bg_gray))
        self.label.setAutoFillBackground(True)
        self.label.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontSliderApp()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())