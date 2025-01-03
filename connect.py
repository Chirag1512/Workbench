import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget

def function():
    print("this function has been called....!!")

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

text = QLabel('This is the main label')
layout.addWidget(text)

button = QPushButton("Click me")
button.clicked.connect(function)
layout.addWidget(button)

window.setLayout(layout)
window.setWindowTitle("Main Window")
window.show()

sys.exit(app.exec())