import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

# 클래스 OOP
class qPushButton(QWidget):
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    # 화면정의를 위한 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 100, 640, 400)
        self.setWindowTitle('QPushbutton')
        self.show()
    
    def addControls(self) -> None:
        btn1 = QPushButton('Click', self)
        btn1.setGeometry(510, 350, 120, 40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qPushButton()
    app.exec_()