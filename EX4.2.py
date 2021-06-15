import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QLabel


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtnHost = QRadioButton('호스트', self)
        rbtnHost.setChecked(True)
        # 호스트 버튼
        rbtnClient = QRadioButton(self)
        rbtnClient.setText('클라이언트')
        # 클라이언트 버튼

        pbtnCrop = QPushButton('Crop', self)
        pbtnPlay = QPushButton('Play', self)
        pbtnStop = QPushButton('Stop', self)
        # 크롭, 공유시작, 정지 버튼

        labelImg = QLabel(self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(rbtnHost)
        hbox.addWidget(rbtnClient)
        hbox.addStretch(1)
        hbox.addWidget(pbtnCrop)
        hbox.addWidget(pbtnPlay)
        hbox.addWidget(pbtnStop)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(labelImg)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
