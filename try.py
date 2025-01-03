"""import sys 
from PySide6.QtCore import QSize,Qt
from PySide6.QtWidgets import QApplication,QPushButton,QMainWindow
class main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Main Window')

        button = QPushButton('click me')
        self.setFixedSize(QSize(100,50))
        self.setCentralWidget(button)
        button.clicked.connect(self.click)

    def click(self):
        print('button click')

app = QApplication(sys.argv)

window = main()
window.show()

app.exec()"""
"""
import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()"""


import sys
from PySide6.QtWidgets import QApplication,QLabel,QMainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lable = QLabel('Click to the window')
        self.setCentralWidget(self.lable)

    def moveevent(self,e):
        self.lable.setText('mouse move event')

    def mousepress (self,e):
        self.lable.setText('mouse press event')
    
    def mouseRelease (self,e):
        self.lable.setText('mouse release event')

    def mouseDoubleClick (self,e):
        self.lable.setText('mouse double click event')

app = QApplication(sys.argv)

window = Main()
window.show()

app.exec()