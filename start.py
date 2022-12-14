#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from time import sleep

from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication, QTextEdit)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        self.text = QTextEdit(self)
        self.text.move(10, 120)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        # print(1)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(1, self)
            self.btn.setText('Stop')
            self.fib(100)

    def fib(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
            self.text.setPlainText(str(b))
            self.step = self.step + 100 / n
            self.pbar.setValue(int(self.step))
            # sleep(0.05)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
