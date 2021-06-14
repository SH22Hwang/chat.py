import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QRadioButton
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.toolbar = self.addToolBar('Exit')
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        playScreenAction = QAction(QIcon('play.png'), 'PlayScreen', self)
        playScreenAction.setShortcut('Ctrl+P')
        playScreenAction.setStatusTip('선택된 화면을 재생한다.')
        playScreenAction.triggered.connect(qApp.quit)

        stopScreenAction = QAction(QIcon('stop.png'), 'StopScreen', self)
        stopScreenAction.setShortcut('Ctrl+D')
        stopScreenAction.setStatusTip('화면공유를 멈춘다.')
        stopScreenAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(playScreenAction)
        # self.toolBar.addAction(self, stopScreenAction)

        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')

        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())