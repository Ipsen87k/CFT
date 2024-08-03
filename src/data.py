from enum import Enum
import pathlib

import util

class _Const(Enum):
    PERMINDEX= 0
    SIZEINDEX = 4
    MONTHINDEX = 5
    TIMEINDEX = 7
    FILENAMEINDEX = 8

    FILEFLAG = "-"
    DIRFLAG = "d"
    SYMBOLICFLAG = "l"

class EntryType(Enum):
    FILE = 0
    DIR = 1
    LINK = 2

class Entry:
    def __init__(self,perm:str,path:str,modiy_time:str,size:int,entry_type:str) -> None:
        self._perm = perm
        self._path = path
        self._modiy_time = modiy_time
        self._size = size
        self._check_entry_type(entry_type)
        self._name = pathlib.Path(path).name


    def __str__(self) -> str:
        return f"{self._perm}\t{self._name}\t{self._modiy_time}\t{self._size}\t{self._entry_type}"
    
    @property
    def perm(self):
        return self._perm
    
    @property
    def path(self):
        return self._path

    @property
    def name(self):
        return self._name

    @property
    def modiy_time(self):
        return self._modiy_time
    
    @property
    def entry_type(self):
        return self._entry_type

    @property
    def size(self):
        return self._size
    
    def _check_entry_type(self,entry_type):
        if _Const.FILEFLAG.value == entry_type:
            self._entry_type = EntryType.FILE
        elif _Const.DIRFLAG.value == entry_type:
            self._entry_type = EntryType.DIR
        else:
            self._entry_type = EntryType.LINK
    
    @staticmethod
    def create_instance(info_str:str,path:str):
        temp_split_arr = info_str.split()
        if len(temp_split_arr) == 0:
            return
        return Entry(temp_split_arr[_Const.PERMINDEX.value],util.path_join_slash(path,temp_split_arr[_Const.FILENAMEINDEX.value]),\
                ":".join(temp_split_arr[_Const.MONTHINDEX.value:_Const.TIMEINDEX.value + 1]),\
                temp_split_arr[_Const.SIZEINDEX.value],\
                temp_split_arr[_Const.PERMINDEX.value][0])
    
if __name__ == '__main__':
    e = EntryType.DIR
    