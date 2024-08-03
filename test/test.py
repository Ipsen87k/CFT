from PySide6 import QtWidgets
import sys
import os
from PySide6.QtCore import QEvent,Qt
from PySide6.QtGui import QKeyEvent

if __name__=='__main__':
    current_dir = os.getcwd()
    current_dir = current_dir[0:len(current_dir)-4]
    src_package_path = os.path.join(current_dir,'src')
    sys.path.append(src_package_path)
    import mainwindow
    import test_connect_win

    class TestMainWin(mainwindow.MainWindow):
        def __init__(self):
            super().__init__()
            #self.current_ui.remoteFileTreeWidget.installEventFilter(self)
            self.secondary_window.activateWindow()

        def open_secondary_window(self):
            self.secondary_window = test_connect_win.TestConnectView(self.communicator)
            self.secondary_window.show()
            self.communicator.client_signal.connect(self.receive_infos_from_secondary_window)

        def eventFilter(self,src,event):
            print(event.type())

        def keyPressEvent(self, event: QKeyEvent) -> None:
            if event.key() == Qt.Key.Key_Control:
                #self.current_ui.remoteFileTreeWidget.setSelectionMode(QtWidgets.QTreeWidget.SelectionMode.MultiSelection)
                pass

        def keyReleaseEvent(self, event: QKeyEvent) -> None:
            if event.key() == Qt.Key.Key_Control:
                #self.current_ui.remoteFileTreeWidget.setSelectionMode(QtWidgets.QTreeWidget.SelectionMode.SingleSelection)
                pass

    app = QtWidgets.QApplication()

    win = TestMainWin()
    win.show()

    sys.exit(app.exec())