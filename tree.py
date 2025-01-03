import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

data = {
    "project A": ["file1.txt", "file2.mp4", "file3.jpg"],
    "project B": ["abc.py", "xyz.txt", "123.png"],
    "project C": [""]
}

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)
        self.setWindowTitle("Login Page")

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "admin" and password == "admin":
            self.redirect_to_welcome()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def redirect_to_welcome(self):
        self.welcome_page = WelcomePage()
        self.welcome_page.show()
        self.close()

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.welcome_ui()

    def welcome_ui(self):
        layout = QVBoxLayout()
        self.welcome_label = QLabel("Welcome to the application!")
        layout.addWidget(self.welcome_label)
        self.setLayout(layout)
        self.setWindowTitle("Welcome Page")
        
        self.msg = QLabel("Hello chirag this is the additional text")
        layout.addWidget(self.msg)

app = QApplication(sys.argv)
tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])

items = []

for key, values in data.items():
    item = QTreeWidgetItem([key])
    for value in values:
        ext = value.split(".")[-1].upper()
        child = QTreeWidgetItem([value, ext])
        item.addChild(child)
    items.append(item)
tree.insertTopLevelItems(0, items)

tree.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())
sys.exit(app.exec_())