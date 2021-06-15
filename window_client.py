from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QRadioButton, QPushButton, QHBoxLayout, \
    QListWidget, QTextEdit, QDesktopWidget
from PyQt5.QtGui import QPixmap, QIcon
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("화면공유 프로그램")
        self.setWindowIcon(QIcon('icon.png'))
        self.center()
        self.displayWidth = 640
        self.displayHeight = 480

        # create the label that holds the image
        self.imgFrame = QLabel(self)
        self.imgFrame.resize(self.displayWidth, self.displayHeight)

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.imgFrame)

        # 호스트 버튼
        rbtnHost = QRadioButton('호스트', self)
        rbtnHost.setChecked(True)
        # 클라이언트 버튼
        rbtnClient = QRadioButton(self)
        rbtnClient.setText('클라이언트')
        # 크롭, 공유시작, 정지 버튼
        pbtnCrop = QPushButton(QIcon('crop.png'), '', self)
        pbtnPlay = QPushButton(QIcon('play.png'), '', self)
        pbtnStop = QPushButton(QIcon('stop.png'), '', self)

        # 버튼 모은 박스
        btnBox = QHBoxLayout()
        btnBox.addWidget(rbtnHost)
        btnBox.addWidget(rbtnClient)
        btnBox.addStretch(1)
        btnBox.addWidget(pbtnCrop)
        btnBox.addWidget(pbtnPlay)
        btnBox.addWidget(pbtnStop)
        # 영상, 버튼 박스 (왼쪽)
        leftBox = QVBoxLayout()
        leftBox.addWidget(self.imgFrame)
        leftBox.addLayout(btnBox)

        # 채팅창
        chatBox = QVBoxLayout()
        recvChat = QListWidget()
        recvChat.setFixedWidth(300)
        sendChat = QTextEdit()
        sendChat.setFixedHeight(25)
        sendChat.setFixedWidth(300)
        # 채팅창 박스
        chatBox.addWidget(recvChat)
        chatBox.addWidget(sendChat)
        # self.sendbtn.clicked.connect(self.sendMsg)
        # 엔터 누르면 보내는 것으로 변경

        # 전체 박스
        box = QHBoxLayout()
        box.addLayout(leftBox)
        box.addLayout(chatBox)

        # set the vbox layout as the widgets layout
        self.setLayout(box)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.imgFrame.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.displayWidth, self.displayHeight, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())
