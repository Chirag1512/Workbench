from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Checkbox Example")
        
        layout = QVBoxLayout()

        self.checkbox = QCheckBox("Check me!")

        layout.addWidget(self.checkbox)

        self.setLayout(layout)

if __name__ == "__main__":
 
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())