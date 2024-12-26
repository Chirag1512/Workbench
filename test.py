#explan me how to to write pyside6 program
# 1. import the necessary modules
# 2. create a QApplication object
# 3. create a QWidget object
# 4. create a layout object
# 5. create the necessary widgets
# 6. add the widgets to the layout
# 7. set the layout to the QWidget object
# 8. set the title of the window
# 9. show the window
# 10. run the application
# 11. handle events
# 12. run the application

#writting the code
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox


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

        self.name = QLabel("HELI PATel")
        layout.addWidget(self.name)
        
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())