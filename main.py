from controller import *
from PyQt5 import *
import sys


def main():
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle('Welcome!')
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
