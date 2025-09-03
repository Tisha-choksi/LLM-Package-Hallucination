import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Notepad")
        self.setGeometry(100, 100, 600, 400)

        # Create text edit area
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Create menu bar
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")

        # Create actions
        self.open_action = QAction("Open", self)
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("Save", self)
        self.save_action.triggered.connect(self.save_file)

        self.exit_action = QAction("Exit", self)
        self.exit_action.triggered.conne
