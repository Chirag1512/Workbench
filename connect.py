import sys
from PySide6.QtWidgets import QApplication, QPushButton

def function():
    print("this function has been called....!!")

app = QApplication()
button = QPushButton("Click me")
button.clicked.connect(function)
button.show()
sys.exit(app.exec_())