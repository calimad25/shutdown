import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def shutdown_1800():
    return os.system(f"shutdown -s -t 1800")


def shutdown_3600():
    return os.system(f"shutdown -s -t 3600")


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shutdown App")

        box = QVBoxLayout()

        button1 = QPushButton("30 min")
        button1.clicked.connect(shutdown_1800)
        button2 = QPushButton("1 hour")
        button2.clicked.connect(shutdown_3600)

        box.addWidget(button1)
        box.addWidget(button2)

        self.setLayout(box)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
