import random
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtWidgets import (
    QApplication, 
    QLabel, 
    QMainWindow,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QRadioButton,
    QGroupBox
)

SPRAY_PARTICLES = 100
SPAY_DIAMETER = 10
COLORS = [  
  "#000000",
  "#141923",
  "#414168",
  "#3a7fa7",
  "#35e3e3",
  "#8fd970",
  "#5ebb49",
  "#458352",
  "#dcd37b",
  "#fffee5",
  "#ffd035",
  "#cc9245",
  "#a15c3e",
  "#a42f3b",
  "#f45b7a",
  "#c24998",
  "#81588d",
  "#bcb0c2",
  "#ffffff",
]

class QPaletteButton(QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QSize(24, 24))
        self.color = color
        self.setStyleSheet(f"background-color: {self.color}")



class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self._pixmap = QPixmap(700, 400)
        self._pixmap.fill(Qt.white)
        self.setPixmap(self._pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QColor("#000000")
        self.pen = True
        self.spray = False

    def set_pen_color(self, c):
        self.pen_color = QColor(c)

    def set_pen(self):
        self.pen = True
        self.spray = False
    
    def set_spray(self):
        self.pen = False
        self.spray = True
        
    def mouseMoveEvent(self, e):
        pos = e.position()
        painter = QPainter(self._pixmap)
        p = painter.pen()
        p.setColor(self.pen_color)
        
        if self.pen:
            if self.last_x is None:
                self.last_x = pos.x()
                self.last_y = pos.y()
                
            p.setWidth(4)
            painter.setPen(p)
            painter.drawLine(self.last_x, self.last_y, pos.x(), pos.y())
            painter.end()
            self.setPixmap(self._pixmap)

            self.last_x = pos.x()
            self.last_y = pos.y()
        if self.spray:
            p.setWidth(1)
            painter.setPen(p)

            for n in range(SPRAY_PARTICLES):
                xo = random.gauss(0, SPAY_DIAMETER)
                yo = random.gauss(0, SPAY_DIAMETER)
                painter.drawPoint(pos.x() + xo, pos.y() + yo)
            self.setPixmap(self._pixmap)

    def mouseReleaseEvent(self, event):
        self.last_x = None
        self.last_y = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()
        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QHBoxLayout()
        self.group_box = QGroupBox()
        self.r_button_pen = QRadioButton('Pen', self.group_box)
        self.r_button_spray = QRadioButton('Spray', self.group_box)
        self.r_button_pen.setChecked(True)
        self.r_button_pen.toggled.connect(self.canvas.set_pen)
        self.r_button_spray.toggled.connect(self.canvas.set_spray)
        palette.addWidget(self.r_button_pen)
        palette.addWidget(self.r_button_spray)

        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
