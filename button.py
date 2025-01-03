import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton

def hello():
    print("hello chirag")

app = QApplication(sys.argv)

button = QPushButton('click me')
button.clicked.connect(hello)
button.show()
sys.exit(app.exec())