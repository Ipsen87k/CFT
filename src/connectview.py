from PySide6.QtGui import QIntValidator
from connectwindow import Ui_CFTConnectWindow
from mq_widgets import MQCommunicator
from client import Client
from sftp_client import SFTPClient
import util

from PySide6.QtWidgets import QMainWindow,QFileDialog

import sys



class ConnectView(QMainWindow):
    def __init__(self,communicator:MQCommunicator=None) -> None:
        super().__init__()
        

        self.communicator = communicator
        self.ui = Ui_CFTConnectWindow()
        self.ui.setupUi(self)

        self.ui.portLineEdit.setValidator(QIntValidator())
    
    def pravateKeyButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self,"Select File")
        if fname[0]:
            self.ui.privateKeyPathLineEdit.setText(fname[0])

    def radioButtonSelected(self):
        if self.ui.passwordRadioButton.isChecked():
            self.ui.privateKeyPathLineEdit.setDisabled(True)
            self.ui.privateKeyButton.setDisabled(True)
        elif self.ui.privateKeyRadioButton.isChecked():
            self.ui.privateKeyPathLineEdit.setDisabled(False)
            self.ui.privateKeyButton.setDisabled(False)

    def finishButtoncClicked(self):
        self.close()

    def connectButtonClicked(self):

        if self.ui.passwordRadioButton.isChecked():
            client = SFTPClient(self.ui.hostLineEdit.text(),self.ui.userLineEdit.text(),\
                                self.ui.passwordLineEdit.text(),int(self.ui.portLineEdit.text()))
        elif self.ui.privateKeyRadioButton.isChecked():
            client = SFTPClient(self.ui.hostLineEdit.text(),self.ui.userLineEdit.text(),\
                                self.ui.passwordLineEdit.text(),int(self.ui.portLineEdit.text()),self.ui.privateKeyPathLineEdit.text())
        
        if client.err:
            util.error_dialog_show(client.err)
            return

        
        result = client.connect()
        if result.is_err():
            util.error_dialog_show(result.err)
            return
        
        self.communicator.client_signal.emit(client)
        self.close()


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("Main Window")
        
#         layout = QVBoxLayout()
        
#         self.open_button = QPushButton("Open Secondary Window")
#         layout.addWidget(self.open_button)
        
#         self.text_input = QLineEdit()
#         layout.addWidget(self.text_input)
        
#         container = QWidget()
#         container.setLayout(layout)
        
#         self.setCentralWidget(container)
        
#         self.open_button.clicked.connect(self.open_secondary_window)
        
#         self.communicator = MQCommunicator()
        
#     def open_secondary_window(self):
#         self.secondary_window = ConnectView(self.communicator)
#         self.secondary_window.show()
        
#         self.communicator.client_signal.connect(self.receive_text)
        
#     def receive_text(self, client:Client):
#         print(client.host,client.path)
#         client.exit()

# import sys
# if __name__ == '__main__':
#     app = QApplication([])
#     ex = MainWindow()
#     ex.show()
#     sys.exit(app.exec())
