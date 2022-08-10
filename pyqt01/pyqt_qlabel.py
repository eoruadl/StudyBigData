import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# 클래스 OOP
class qFont(QWidget):
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    # 화면정의를 위한 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 500, 400)
        self.setWindowTitle('QLabel')
        self. text = 'What a wonderful world~'
        self.show()

    def addControls(self) -> None:
        label1 = QLabel('Label1', self)
        label2 = QLabel('Label2', self)
        label1.setStyleSheet(
            ('border-width: 3px;'
            'border-style: solid;'
            'border-color: blue;'
            'image: url(./pyqt01/image/image1.png)')
        )

        label2.setStyleSheet(
            ('border-width: 3px;'
            'border-style: dot-dot-dash;'
            'border-color: green;'
            'image: url(./pyqt01/image/image2.png)')
        )

        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qFont()
    app.exec_()