import os
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout


def shutdown():
    return os.system(f"shutdown -s -t 3600")


app = QApplication([])

window = QWidget()
window.setWindowTitle("Shutdown App")
layout = QVBoxLayout()

button = QPushButton("Shutdown")
button.clicked.connect(shutdown)

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)

window.show()
sys.exit(app.exec())
