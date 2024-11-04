
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication , QWidget, QMainWindow, QLabel ,QPushButton, QMenu
import sys
from PyQt6.QtGui import QFont , QIcon ,QPixmap 
#QMainWndow
#QWidget
#QDialog

class MyWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setMaximumSize(800,800)
        self.setMinimumSize(400,400)
        self.setWindowOpacity(1)
        self.setWindowTitle('Fatemeh')
        self.label= QLabel("hello" , self)
        #self.label.move(40,40)
        #self.label.setFont(QFont('Arial',20))
        #image = QPixmap(r'C:\Users\Lenovo\Desktop\prj_PyQt\logo.png').scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio)
        #self.label.setPixmap(image)
        #self.label.resize(300, 300)
        self.button = QPushButton('Qpushbutton', self)
        self.button.setGeometry(200, 10, 100, 50)
        self.button.setFont(QFont('Aria', 5))
        self.button.setIcon(QIcon('logo.png'))

        menue = QMenu()
        menue.addAction('copy')
        menue.addAction('paste')
        menue.addAction('out')
        self.button.setFont(QFont('Aria', 5))
        menue.setStyleSheet("background-color:red")
        self.button.setMenu(menue)




app=QApplication(sys.argv)
window= MyWindow()
window.show()
sys.exit(app.exec())