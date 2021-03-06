from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QToolTip, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.resize(1000, 1000)
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle('直播压力测试')
        self.setWindowIcon(QIcon('favicon.ico'))
        # self.getText()
        self.url_edit = QLineEdit(self)
        self.url_edit.setPlaceholderText('请输入url')
        self.url_edit.setGeometry(5, 5, 800, 20)
        self.nums_edit = QLineEdit(self)
        self.nums_edit.setPlaceholderText('nums')
        self.nums_edit.setGeometry(820, 5, 40, 20)
        # self.label = QLabel(self)
        # self.label.setGeometry(20, 20, 200, 20)
        # print(self.url_edit)
        btn = QPushButton('新建窗口', self)
        btn.setToolTip('新建直播窗口')
        btn.move(900, 5)
        # btn.resize(btn.sizeHint())
        view = QWebEngineView(self)
        view.load(QUrl("https://192.168.20.120/videoroomtest.html?subscriber-mode=true"))
        view.setGeometry(30, 30, 800, 800)
        # _player = QMediaPlayer(self)
        # _videoSurface =
        self.setGeometry(0, 0, 1000, 1000)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def getText(self):
    #     text, okPressed = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Normal, "")
    #     if okPressed and text != '':
    #         print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
