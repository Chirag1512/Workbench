#create basic window for pyside6
import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Main Window")
window.setFixedSize(400,200) 
window.show()

sys.exit(app.exec())

