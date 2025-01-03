import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QDateEdit, QWidget, QVBoxLayout, QMessageBox, QComboBox, QRadioButton, QBoxLayout

class DateWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(500)
        self.setStyleSheet('''QWidget{
                           font-size:30px
                           }''')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.dateEdit = QDateEdit()
        layout.addWidget(self.dateEdit)

        self.button = QPushButton('click me')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.hello)
        self.combo = QComboBox()
        self.combo.currentIndexChanged.connect(self.change_page)
        self.combo.addItems(['Section 1', 'Section 2', 'Section 3'])
        layout.addWidget(self.combo)

        self.pages = [self.create_page1(), self.create_page2(), self.create_page3()]
        for page in self.pages:
            layout.addWidget(page)
            page.hide()
        self.pages[0].show()

        self.rdo(layout)

    def hello(self):
        msg = QMessageBox() 
        msg.setText('Hello')
        msg.exec()

    def change_page(self, index):
        for page in self.pages:
            page.hide()
        self.pages[index].show()

    def create_page1(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)
        layout.addWidget(QLabel("This is Page 1"))
        return page

    def create_page2(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)
        layout.addWidget(QLabel("This is Page 2"))
        return page

    def create_page3(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)
        layout.addWidget(QLabel("This is Page 3"))
        return page

    def rdo(self, layout):
        rd1 = QRadioButton('Radio Button 1')
        rd2 = QRadioButton('Radio Button 2')
        rd3 = QRadioButton('Radio Button 3')
        layout.addWidget(rd1)
        layout.addWidget(rd2)
        layout.addWidget(rd3)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = DateWidget()
    demo.show()

    try:
        sys.exit(app.exec())
    except:
        print('closing the window')
