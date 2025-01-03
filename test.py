import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QMessageBox, QFileDialog, QMenu
from PySide6.QtGui import QAction
from PySide6.QtPrintSupport import QPrinter

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        new_text_action = QAction("New Text File", self)
        new_text_action.triggered.connect(self.new_file)

        new_python_action = QAction("New Python File", self)
        new_python_action.triggered.connect(self.new_python_file)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)

        pdf_action = QAction("Export as PDF", self)
        pdf_action.triggered.connect(self.export_as_pdf)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)

    
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        new_menu = QMenu("New", self)
        new_menu.addAction(new_text_action)
        new_menu.addAction(new_python_action)

        file_menu.addMenu(new_menu)
        file_menu.addAction(save_action)
        file_menu.addAction(open_action)
        file_menu.addAction(pdf_action)
        file_menu.addAction(exit_action)

        self.setWindowTitle("Text Editor")
        self.show()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        new_text_action = QAction("New Text File", self)
        new_text_action.triggered.connect(self.new_file)

        new_python_action = QAction("New Python File", self)
        new_python_action.triggered.connect(self.new_python_file)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)

        pdf_action = QAction("Export as PDF", self)
        pdf_action.triggered.connect(self.export_as_pdf)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)

    
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        new_menu = QMenu("New", self)
        new_menu.addAction(new_text_action)
        new_menu.addAction(new_python_action)

        file_menu.addMenu(new_menu)
        file_menu.addAction(save_action)
        file_menu.addAction(open_action)
        file_menu.addAction(pdf_action)
        file_menu.addAction(exit_action)

        self.setWindowTitle("Text Editor")
        self.show()
        
    def new_file(self):
        self.text_edit.clear()

    def new_python_file(self):
        self.text_edit.clear()
        self.current_file_extension = ".py"

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", filter="Python Files (*.py);;All Files (*)")
        if file_path:
            if hasattr(self, 'current_file_extension') and not file_path.endswith(self.current_file_extension):
                file_path += self.current_file_extension
            with open(file_path, "w") as file:
                file.write(self.text_edit.toPlainText())

    def open_file(self):

        
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_path:
            with open(file_path, "r") as file:
                self.text_edit.setPlainText(file.read())

    def export_as_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Export as PDF", filter="PDF Files (*.pdf);;All Files (*)")
        if file_path:
            if not file_path.endswith(".pdf"):
                file_path += ".pdf"
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(file_path)
            self.text_edit.document().print_(printer)

    def exit_app(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    text_editor = TextEditor()
    sys.exit(app.exec())


