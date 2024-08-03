from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtCore import QObject,Signal

from data import EntryType
from client import Client

class MQTreeWidgetFileItem(QTreeWidgetItem):
    def __init__(self,path:str):
        super().__init__()
        self._path = path

    def setEntryType(self,entryType:EntryType):
        self._entryType = entryType

    def entryType(self)->EntryType:
        return self._entryType

    def path(self)->str:
        return self._path

class MQCommunicator(QObject):
    client_signal = Signal(Client)