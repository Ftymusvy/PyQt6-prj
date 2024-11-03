
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication , QWidget, QMainWindow
import sys
#QMainWndow
#QWidget
#QDialog

class MyWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.menuBar().addMenu('file')
        self.statusBar().showMessage('Hello')

app=QApplication(sys.argv)
window= MyWindow()
window.show()
sys.exit(app.exec())