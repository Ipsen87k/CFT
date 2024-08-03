import paramiko
from paramiko.pkey import UnknownKeyType
from client import Client
from util import Result
import util
from data import Entry

from paramiko.ssh_exception import (BadHostKeyException,
                                    NoValidConnectionsError,
                                    AuthenticationException,
                                    SSHException
                                    )
from paramiko.sftp import SFTPError
import socket

class SFTPClient(Client):
    def __init__(self, host: str, user: str, password: str,port:int,private_key_file=None):
        super().__init__(host, user, password,port)
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._key = private_key_file
        self.err = None
        if private_key_file:
            try:
                if len(password) > 0:
                    self._key = paramiko.PKey.from_path(private_key_file,self._password.encode())
                else:
                    self._key = paramiko.PKey.from_path(private_key_file)
            except Exception as e:
                self.err = e

    def connect(self) -> Result:
        try:
            self._client.connect(self._host,username=self._user,password=self._password,pkey=self._key,port=self._port)
            self._ftp = self._client.open_sftp()

            self._ftp.chdir('.')
            self._path = self._ftp.getcwd()
        except BadHostKeyException as e:
            return Result(err=e)
        except NoValidConnectionsError as e:
            return Result(err=e)
        except AuthenticationException as e:
            return Result(err=e)
        except SSHException as e:
            return Result(err=e)
        except SFTPError as e:
            return Result(err=e)
        except socket.error as e:
            return Result(err=e)

        
        return Result().ok()
    
    def exit(self):
        self._ftp.close()
        self._client.close()
    
    def get_entries(self, path=".") -> Result:
        try:
            return Result(value=[Entry.create_instance(e.longname,path) for e in self._ftp.listdir_attr(path)])
        except SFTPError as e:
            if str(e) == 'None':
                return Result(value=[])
            return Result(err=e)
        
    def cd(self, path: str) -> Result:
        try:
            self._ftp.chdir(path)
            self._path = self._ftp.getcwd()
            return Result().ok()
        except IOError as e:
            return Result(err=e)

    def download_file(self, path: str, save_path=".") -> Result:
        try:
            self._ftp.get(path,util.path_join_slash(save_path,util.get_file_name(path)))
            return Result().ok()
        except IOError as e:
            return Result(err=e)

    def send_file(self, fname: str) -> Result:
        try:
            self._ftp.put(fname,util.path_join_slash(self._path,util.get_file_name(fname)))
            return Result().ok()
        except IOError as e:
            return Result(err=e)
if __name__ == '__main__':

    print(type(8))