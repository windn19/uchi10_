import sys
from time import sleep

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QBasicTimer


class Text(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        self.btn = QPushButton('Start')
        self.btn.clicked.connect(self.click_btn)
        self.text = QTextEdit()
        self.lbl = QLabel('')
        vbox.addWidget(self.btn)
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.text)

        self.timer = QBasicTimer()
        self.step = 0
        self.b = 0


        self.setLayout(vbox)
        self.setWindowTitle('Вывод чисел Фиббоначи')
        self.setGeometry(300, 300, 500, 400)

    def fib(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
            self.text.insertPlainText(f'\n{b}')
            # sleep(0.01)
        self.text.insertPlainText('\nStop')
        self.timer.stop()

    def click_btn(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(1, self)
            self.btn.setText('Stop')
            self.fib(1000)

    def timerEvent(self, e):
        self.text.insertPlainText(f'\n{self.b}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Text()
    win.show()
    sys.exit(app.exec_())
