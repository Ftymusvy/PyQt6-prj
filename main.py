
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication , QWidget, QMainWindow
import sys
#QMainWndow
#QWidget
#QDialog

class MyWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setMaximumSize(500,500)
        self.setMinimumSize(100,100)
        self.setWindowOpacity(0.5)
        self.setWindowTitle('Fatemeh')

app=QApplication(sys.argv)
window= MyWindow()
window.show()
sys.exit(app.exec())