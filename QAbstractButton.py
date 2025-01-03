import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractButton, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import QSize

class CustomButton(QAbstractButton):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)

    def paintEvent(self, event):
        # Custom paint code can go here
        pass

    def sizeHint(self):
        return QSize(100, 30)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QAbstractButton Example")

        layout = QVBoxLayout()

        button1 = CustomButton("Custom Button")
        button1.clicked.connect(self.on_button_clicked)
        layout.addWidget(button1)

        button2 = QPushButton("QPushButton")
        button2.clicked.connect(self.on_button_clicked)
        layout.addWidget(button2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_clicked(self):
        print("Button clicked!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()