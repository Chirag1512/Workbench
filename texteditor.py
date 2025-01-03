import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QAction

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)

        print_action = QAction("Print", self)
        print_action.triggered.connect(self.print_file)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        file_menu.addAction(open_action)
        file_menu.addAction(print_action)
        file_menu.addAction(exit_action)

        self.setWindowTitle("Text Editor")
        self.show()

    def new_file(self):
        self.text_edit.clear()

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_edit.toPlainText())

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_path:
            with open(file_path, "r") as file:
                self.text_edit.setPlainText(file.read())

    def print_file(self):
        pass

    def exit_app(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    text_editor = TextEditor()
    sys.exit(app.exec())


