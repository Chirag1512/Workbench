import sys

from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

"""class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        combobox = QComboBox()
        combobox.addItems(["One", "Two", "Three"])

        # The default signal from currentIndexChanged sends the index
        combobox.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        combobox.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(combobox)

    def index_changed(self, index):  # index is an int starting from 0
        print(index)

    def text_changed(self, text):  # text is a str
        print(text)"""
"""class MainWindow(QMainWindow):"""

def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")


    self.lineedit = QLineEdit()
    self.lineedit.setMaxLength(10)
    self.lineedit.setPlaceholderText("Enter your text")

    self.lineedit.returnPressed.connect(self.return_pressed)
    self.lineedit.selectionChanged.connect(self.selection_changed)
    self.lineedit.textChanged.connect(self.text_changed)
    self.lineedit.textEdited.connect(self.text_edited)

    self.setCentralWidget(self.lineedit)

def return_pressed(self):
    print("Return pressed!")
    self.lineedit.setText("BOOM!")

def selection_changed(self):
    print("Selection changed")
    print(self.lineedit.selectedText())

def text_changed(self, text):
    print("Text changed...")
    print(text)

def text_edited(self, text):
    print("Text edited...")
    print(text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        dial = QDial()
        dial.setRange(-10, 100)
        dial.setSingleStep(1)

        dial.valueChanged.connect(self.value_changed)
        dial.sliderMoved.connect(self.dial_position)
        dial.sliderPressed.connect(self.dial_pressed)
        dial.sliderReleased.connect(self.dial_released)

        self.setCentralWidget(dial)

    def value_changed(self, value):
        print(value)

    def dial_position(self, position):
        print("position", position)

    def dial_pressed(self):
        print("Pressed!")

    def dial_released(self):
        print("Released")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()