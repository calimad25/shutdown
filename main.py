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

        button1 = QPushButton("Now")
        button1.clicked.connect(lambda x: shutdown(1))
        button2 = QPushButton("30 min")
        button2.clicked.connect(lambda x: shutdown(1800))
        button3 = QPushButton("1 hour")
        button3.clicked.connect(lambda x: shutdown(3600))
        button4 = QPushButton("2 hours")
        button4.clicked.connect(lambda x: shutdown(7200))
        button6 = QPushButton("Cancel Shutdown")
        button6.clicked.connect(cancel_shutdown)

        box.addWidget(button1)
        box.addWidget(button2)
        box.addWidget(button3)
        box.addWidget(button4)
        box.addWidget(button6)

        self.setLayout(box)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
