
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication , QWidget, QMainWindow, QLabel ,QPushButton, QMenu,QLineEdit, QHBoxLayout
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
        
        self.create_qline_edit()
        self.clicked()


    def create_qline_edit(self):
        self.input_text= QLineEdit(self)
        self.input_text.setPlaceholderText('enter your name')
        self.input_text.setText("default")
        self.input_text.setStyleSheet('color:blue')
        self.input_text.setEchoMode(QLineEdit.EchoMode.Password)
    def clicked(self):
        if self.input_text.text():
            self.label.setText(self.input_text.text())
            self.input_text.clear()


app=QApplication(sys.argv)
window= MyWindow()
window.show()
sys.exit(app.exec())