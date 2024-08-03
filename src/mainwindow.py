from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent,QIcon,QPixmap
from PySide6.QtWidgets import QFileDialog,QTreeWidgetItem,QFileSystemModel,QListWidgetItem
from PySide6.QtCore import QDir

import pathlib
import os

from data import EntryType,Entry
from sftp_client import SFTPClient
from mq_widgets import MQTreeWidgetFileItem,MQCommunicator
from client import Client
import util
#from ftp_test import get_user_pass
import qt_mainui
import icons_rc
from connectview import ConnectView

#from test_gui import TestConnectView


class MainWindow(QtWidgets.QMainWindow):
    QTreeHeaderItem = QTreeWidgetItem(["Name","Size","Date Modified","Perm"])

    def __init__(self):
        super().__init__()
        self.file_icon = QIcon(QPixmap(":/icons/file.png"))
        self.dir_icon = QIcon(QPixmap(":/icons/dir.png"))
        self.link_icon = QIcon(QPixmap(":/icons/link.png"))
        self.arrow_icon = QIcon(QPixmap(":/icons/data_transfer_arrow.svg"))
        self.app_icon = QIcon(QPixmap(":icons/app_icon.ico"))
        self.setWindowIcon(self.app_icon)
        self.current_ui = qt_mainui.Ui_MainWindow()
        self.current_ui.setupUi(self)

        self.current_ui.remoteFileTreeWidget.setHeaderItem(self.QTreeHeaderItem)
        self.current_ui.remoteFileTreeWidget.setSelectionMode(QtWidgets.QTreeWidget.SelectionMode.ExtendedSelection)


        self.model = QFileSystemModel()
        self.local_save_path = QDir.homePath()
        self.current_ui.localFileTreeView.setModel(self.model)
        self.set_model_path(self.local_save_path)
        self.current_ui.localPathEdit.setText(self.local_save_path)
        self.current_ui.localFileTreeView.setSelectionMode(QtWidgets.QTreeWidget.SelectionMode.ExtendedSelection)

        self.client = None

        self.communicator = MQCommunicator()

        self.open_secondary_window()


    def closeEvent(self,event:QCloseEvent):
        reply = QtWidgets.QMessageBox.question(
            self,
            '確認',
            'プログラムを終了しますか',
            buttons=QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            if self.client:
                self.client.exit()
            event.accept()
        else:
            event.ignore()

    def fileOpen(self):
        dir_name = QFileDialog.getExistingDirectory(self,'Select Folder')
        if dir_name:
            self.set_model_path(dir_name)
            self.current_ui.localPathEdit.setText(dir_name)
            self.local_save_path = dir_name

    def set_model_path(self,path:str="."):
        self.model.setRootPath(path)
        self.current_ui.localFileTreeView.setRootIndex(self.model.index(path))

    def set_remote_entries(self,path:str="."):
        result_entries = self.client.get_entries(path)

        if result_entries.is_err():
            util.error_dialog_show(result_entries.err)
            return

        self.current_ui.remoteFileTreeWidget.clear()
        parent_item = self.create_parent_qtree_item(path)
        self.current_ui.remoteFileTreeWidget.addTopLevelItem(parent_item)

        if len(result_entries.value) > 0:
            qtree_item_list = [self.create_qtree_item(e) for e in result_entries.value]
            parent_item.addChildren(qtree_item_list)
            self.current_ui.remoteFileTreeWidget.expandAll()

        if path == ".":
            self.current_ui.remotePathEdit.setText(self.client.path)
        else:
            self.current_ui.remotePathEdit.setText(path)
        
        self.add_log_line_list_widget('ファイル一覧取得に成功しました。')

    def create_parent_qtree_item(self,path:str)->MQTreeWidgetFileItem:
        if path == ".":
            name = pathlib.Path(self.client.path).name
        else:
            name = pathlib.Path(path).name

        parent_item = MQTreeWidgetFileItem("..")
        parent_item.setEntryType(EntryType.DIR)
        parent_item.setIcon(0,self.dir_icon)
        parent_item.setText(0,name)

        return parent_item

    def create_qtree_item(self,entry:Entry)->MQTreeWidgetFileItem:
        item = MQTreeWidgetFileItem(entry.path)
        if entry.entry_type == EntryType.FILE:
            item.setIcon(0,self.file_icon)
            item.setEntryType(EntryType.FILE)
        elif entry.entry_type == EntryType.DIR:
            item.setIcon(0,self.dir_icon)
            item.setEntryType(EntryType.DIR)
        else:
            item.setIcon(0,self.link_icon)
            item.setEntryType(EntryType.LINK)

        item.setText(0,entry.name)
        item.setText(1,str(entry.size))
        item.setText(2,entry.modiy_time)
        item.setText(3,entry.perm)

        return item

    def itemDoubleClicked(self,item,_column):
        if isinstance(item,MQTreeWidgetFileItem):
            if item.entryType() == EntryType.DIR:
                self.client.cd(item.path())
                self.set_remote_entries(self.client.path)
            elif item.entryType() == EntryType.FILE:
                result = self.client.download_file(item.path(),self.local_save_path)
                if result.is_err():
                    util.error_dialog_show(result.err)
                    return

                self.add_log_line_list_widget(f'{util.get_file_name(item.path())}のダウンロードに成功しました。')

    def remoteEnterPressed(self):
        path = self.current_ui.remotePathEdit.text()
        result = self.client.cd(path)
        if result.is_err():
            util.error_dialog_show(result.err)
            return 
        self.set_remote_entries(path)

    def localPathEnterPressed(self):
        path = self.current_ui.localPathEdit.text()
        if os.path.exists(path) and os.path.isdir(path):
            self.set_model_path(path)
        else:
            util.error_dialog_show(Exception("フォルダが見つかりません"))

    def open_secondary_window(self):
        self.secondary_window = ConnectView(self.communicator)
        self.secondary_window.setWindowIcon(self.app_icon)
        self.secondary_window.show()
        self.secondary_window.activateWindow()
        self.communicator.client_signal.connect(self.receive_infos_from_secondary_window)

    
    def receive_infos_from_secondary_window(self,client:Client):
        self.client = client
        self.add_log_line_list_widget(f'{self.client.host}に接続が成功しました')
        self.set_remote_entries(self.client.path)
    
    def localFileItemDoubleClicked(self,idx):
        file_path = self.model.filePath(idx)
        if os.path.isfile(file_path):
            result = self.client.send_file(file_path)
            if result.is_err():
                util.error_dialog_show(result.err)
                return
            
            self.add_log_line_list_widget(f'{util.get_file_name(file_path)}の送信に成功しました。')
        elif os.path.isdir(file_path):
            pass
        
        #flushのため
        self.set_remote_entries(self.client.path)

    def menuExit(self):
        if self.client:
            self.client.exit()
            self.current_ui.remoteFileTreeWidget.clear()
            self.current_ui.remotePathEdit.clear()
            self.add_log_line_list_widget(f'{self.client.host}から切断しました。')

    def add_log_line_list_widget(self,log:str):
        self.current_ui.logListWidget.addItem(QListWidgetItem(log))

    def menuConnect(self):
        self.open_secondary_window()

    
    def localToRemoteButtonClicked(self):
        #fileModel はnameとsizeとtypeとmodifytimeの4つがあるのでlenでやると4つになるので4の倍数のみ処理
        for i,item in enumerate(self.current_ui.localFileTreeView.selectedIndexes()):
            if i%4==0:
                file_path = self.model.filePath(item)
                if os.path.isfile(file_path):
                    result = self.client.send_file(file_path)
                    if result.is_err():
                        util.error_dialog_show(result.err)
                        return
                    
                    self.add_log_line_list_widget(f'{util.get_file_name(file_path)}の送信に成功しました。')
                elif os.path.isdir(file_path):
                    pass
                
                #flushのため
                self.set_remote_entries(self.client.path)

    def remoteToLocalButtonClicked(self):
        for item in self.current_ui.remoteFileTreeWidget.selectedItems():
            if item.entryType() == EntryType.FILE:
                result = self.client.download_file(item.path(),self.local_save_path)
                if result.is_err():
                    util.error_dialog_show(result.err)
                    return

                self.add_log_line_list_widget(f'{util.get_file_name(item.path())}のダウンロードに成功しました。')