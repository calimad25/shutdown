import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def shutdown(time):
    return os.system(f"shutdown -s -t {time}")


def cancel_shutdown():
    return os.system("shutdown -a")


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shutdown App")
        self.setGeometry(300, 200, 300, 200)

        box = QVBoxLayout()

        button1 = QPushButton("30 min")
        button1.clicked.connect(lambda x: shutdown(1800))
        button2 = QPushButton("1 hour")
        button2.clicked.connect(lambda x: shutdown(3600))
        button3 = QPushButton("2 hours")
        button3.clicked.connect(lambda x: shutdown(7200))
        button4 = QPushButton("Cancel Shutdown")
        button4.clicked.connect(cancel_shutdown)

        box.addWidget(button1)
        box.addWidget(button2)
        box.addWidget(button3)
        box.addWidget(button4)

        self.setLayout(box)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
