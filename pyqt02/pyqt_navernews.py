import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/navernews.ui', self)
        self.initUI()

    # 화면정의를 위한 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        self.show()
    
    def addControls(self) -> None:
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()