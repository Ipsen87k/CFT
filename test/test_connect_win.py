import sys
from PySide6 import QtWidgets
import mainwindow

from connectview import ConnectView
from ftp_test import get_user_pass_privatekey

class TestConnectView(ConnectView):
    def __init__(self, communicator = None) -> None:
        super().__init__(communicator)
        arr = get_user_pass_privatekey()

        self.ui.privateKeyRadioButton.setChecked(True)
        self.ui.privateKeyButton.setEnabled(True)
        self.ui.privateKeyPathLineEdit.setEnabled(True)


        self.ui.hostLineEdit.setText(arr[0])
        self.ui.userLineEdit.setText(arr[1])
        self.ui.passwordLineEdit.setText(arr[2])
        self.ui.privateKeyPathLineEdit.setText(arr[3])


if __name__ =='__main__':
    app = QtWidgets.QApplication(
        sys.argv
    )

    win = mainwindow.TestMainWindow()
    win.show()

    sys.exit(app.exec())