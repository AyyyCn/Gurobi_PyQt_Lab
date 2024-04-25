import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 300, 200)

        # Button for PL
        self.pl_button = QPushButton("PL", self)
        self.pl_button.setGeometry(50, 50, 100, 100)
        self.pl_button.clicked.connect(self.open_pl_window)

        # Button for PLNE
        self.plne_button = QPushButton("PLNE", self)
        self.plne_button.setGeometry(150, 50, 100, 100)
        self.plne_button.clicked.connect(self.open_plne_window)

    def open_pl_window(self):
        self.pl_window = SecondaryWindow("PL")
        self.pl_window.show()

    def open_plne_window(self):
        self.plne_window = SecondaryWindow("PLNE")
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
