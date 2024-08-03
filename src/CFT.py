import sys
from PySide6 import QtWidgets
import os
import mainwindow

if __name__=='__main__':
    with open(os.devnull,'w',encoding='utf-8') as f:
        sys.stderr=f
        sys.stdout = f
        sys.stdin = f

        app = QtWidgets.QApplication(
            sys.argv
        )

        win = mainwindow.MainWindow()
        win.show()

        ret = app.exec()
    sys.exit(ret)
