import ftplib
from util import Result
from client import Client
from data import Entry
from typing import List


class FTPClient(Client):
    def __init__(self, host: str, user: str, password: str) -> None:
        super().__init__(host, user, password)
        self._ftp = ftplib.FTP()

    def connect(self)->Result:
        try:
            self._ftp.connect(self._host)
            self._ftp.login(self._user,self._password)
            self._path = self._ftp.pwd()
        except ftplib.all_errors as e:
            return Result(err=e)

        return Result().ok()
    
    def exit(self):
        self._ftp.quit()

    def get_entries(self, path=".") -> Result:
        try:
            entries = []
            if path == ".":
                self._ftp.dir(entries.append)
            else:
                self._ftp.cwd(path)
                self._ftp.dir(entries.append)
            return Result(value=[Entry.create_instance(e,self._path) for e in entries])
        except ftplib.error_perm as e:
            return Result(err=e)

    def cd(self, path: str) -> Result:
        try:
            self._ftp.cwd(path)
            self._path = self._ftp.pwd()
            return Result().ok()
        except Exception as e:
            return Result(err=e)
    
    def list_files(self):
        try:
            files = []
            self._ftp.dir(files.append)
            print(files)
        except ftplib.error_perm as e:
            return Result(err=e)

        return Result().ok()
    
    def mlsd(self):
        try:
            lis = self._ftp.mlsd()
            for i in lis:
                print(i)
        except ftplib.error_perm as e:
            print('ファイルが見つかりません')


class Test:
    file = ['-rw-r--r--    1 1000     1000          264 Apr 28 03:35 dockerdownload.sh',\
        '-rw-r--r--    1 1000     1000           29 May 24 01:15 last_backup.sh', \
        '-rw-r--r--    1 1000     1000       246601 Apr 26 01:29 sudo_his.log', \
        'drwxr-xr-x    2 1000     1000         4096 Jun 24 02:51 sudoo',\
        'lrwxrwxrwx    1 1000     1000           15 Jun 24 03:03 trs -> ./sudoo/test.rs', \
        'drwxr-xr-x    2 1000     1000         4096 Jun 24 02:54 whoami']
    
    sudoo = ['-rw-r--r--    1 1000     1000            0 Jun 24 02:50 pass_show.py',\
                '-rw-r--r--    1 1000     1000            0 Jun 24 02:50 sudo_login.rs',\
                '-rw-r--r--    1 1000     1000           37 Jun 24 02:51 test.rs']
    
    def test_format_files(self):
        return [Entry.create_instance(f) for f in self.file]
    
    def test_cd_sudoo_files(self):
        return [Entry.create_instance(f) for f in self.sudoo]

    def test_split_files(self):
        for f in self.file:
            tmp = f.split()
            print(tmp[0][0])
