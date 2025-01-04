#write a exapmle of tabbar
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabBar, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox, QMenuBar,QComboBox
from PySide6.QtGui import QPixmap


class TabBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet('''
            QWidget {
                font-size: 20px;
            }
            QTabBar::tab {
                background: lightgray;
                padding: 10px;
            }
            QTabBar::tab:selected {
                background: darkgray;
            }
            QLabel {
                color: darkblue;
            }
            QLineEdit {
                background-color: lightyellow;
                color: black;
            }
            QPushButton {
                background-color: lightblue;
                color: darkgreen;
            }
            QCheckBox {
                font-size: 18px;
            }
            QMenuBar {
                background-color: lightblue;
                color: darkblue;
            }
        ''')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.menu = self.menubar()
        layout.setMenuBar(self.menu)

        self.tab_bar = QTabBar()
        self.tab_bar.addTab('Tab 1')
        self.tab_bar.addTab('Tab 2')
        self.tab_bar.addTab('Tab 3')
        self.tab_bar.currentChanged.connect(self.change_page)
        layout.addWidget(self.tab_bar)

        self.pages = [self.create_page1(), self.create_page2(), self.create_page3(), self.create_page_with_dropdown(), self.create_page4(), self.create_page5()]
        for page in self.pages:
            layout.addWidget(page)
            page.hide()
        self.pages[0].show()

        self.img()

    def change_page(self, index):
        for page in self.pages:
            page.hide()
        self.pages[index].show()

    def create_page1(self):
        page = QWidget()
        self.text = QLabel('<h1>Login</h1>')
        self.email = QLabel("Email")
        self.password = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.email_input = QLineEdit()
        self.password_input = QLineEdit()
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout = QVBoxLayout()
        page.setLayout(layout)
        layout.addWidget(self.text)
        layout.addWidget(self.email)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        return page

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        if email == "admin" and password == "123":
            self.message_box = QMessageBox()
            self.message_box.setText("Login Successful")
            self.message_box.exec()
        else:
            self.message_box = QMessageBox()
            self.message_box.setText("Login Failed")
            self.message_box.exec()

    def create_page2(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)
        self.text = QLabel('<h1>Sign Up </h1>')
        self.name = QLabel("Name")
        self.name_input = QLineEdit()
        self.email = QLabel("Email")
        self.email_input = QLineEdit()
        self.password = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.signup)
        layout.addWidget(self.text)
        layout.addWidget(self.name)
        layout.addWidget(self.name_input)
        layout.addWidget(self.email)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password)
        layout.addWidget(self.password_input)
        layout.addWidget(self.signup_button)
        return page

    def signup(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        print(f"Name: {name}, Email: {email}, Password: {password}")

    def create_page3(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)
        self.checkbox1 = QCheckBox("Option 1")
        self.checkbox2 = QCheckBox("Option 2")
        self.checkbox3 = QCheckBox("Option 3")
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.display_selection)
        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.checkbox3)
        layout.addWidget(self.submit_button)
        return page
    
    def create_page_with_dropdown(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)
        
        self.dropdown_label = QLabel('<h1>Select an Option</h1>')
        self.dropdown = QComboBox()
        self.dropdown.addItems(["Option A", "Option B", "Option C"])
        self.dropdown.currentIndexChanged.connect(self.display_dropdown_selection)
        
        layout.addWidget(self.dropdown_label)
        layout.addWidget(self.dropdown)
        
        self.dropdown_output = QLabel('')
        layout.addWidget(self.dropdown_output)
        
        return page

    def display_dropdown_selection(self, index):
        selected_option = self.dropdown.currentText()
        self.dropdown_output.setText(f"You selected: {selected_option}")
    def display_selection(self):
        selected_options = []
        if self.checkbox1.isChecked():
            selected_options.append("Option 1")
        if self.checkbox2.isChecked():
            selected_options.append("Option 2")
        if self.checkbox3.isChecked():
            selected_options.append("Option 3")

        if selected_options:
            QMessageBox.information(self, "Selection", f"You selected: {', '.join(selected_options)}")
        else:
            QMessageBox.information(self, "Selection", "No options selected")

    def menubar(self):
        menu = QMenuBar(self)
        file_menu = menu.addMenu("File")
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Exit")

        edit_menu = menu.addMenu("Edit")
        edit_menu.addAction("Main_File")
        edit_menu.addAction("Current_File")
        view_menu = menu.addMenu("View")
        view_menu.addAction("Data_File")
        view_menu.addAction("PDF_File")
        help_menu = menu.addMenu("Help")
        help_menu.addAction("System info")
        help_menu.addAction("Service center")
        return menu

        
    def create_page4(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)
        self.text = QLabel('<h1>Page 4</h1>')
        layout.addWidget(self.text)
        return page
    
    def create_page5(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)
        self.text = QLabel('<h1>Page 5</h1>')
        layout.addWidget(self.text)

        return page
    
    def img(self):
        img = QLabel(self)
        pixmap = QPixmap('hello.jpg')
        img.setPixmap(pixmap)
        self.layout().addWidget(img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabBar()
    demo.show()
    sys.exit(app.exec())


