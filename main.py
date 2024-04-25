import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 300, 200)

        # Create a central widget and set it to the main window
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a vertical layout for the buttons
        self.layout = QVBoxLayout(self.central_widget)

        # Button for PL
        self.pl_button = QPushButton("PL")
        self.layout.addWidget(self.pl_button)
        self.pl_button.clicked.connect(self.open_pl_window)

        # Button for PLNE
        self.plne_button = QPushButton("PLNE")
        self.layout.addWidget(self.plne_button)
        self.plne_button.clicked.connect(self.open_plne_window)

    def open_pl_window(self):
        self.pl_window = SecondaryWindow("PL Window")
        self.pl_window.show()

    def open_plne_window(self):
        self.plne_window = SecondaryWindow("PLNE Window")
        self.plne_window.show()

class SecondaryWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 200, 100)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
