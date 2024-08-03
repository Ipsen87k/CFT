from util import Result

class Client:
    def __init__(self,host:str,user:str,password:str,port:int) -> None:
        self._host = host
        self._user = user
        self._password = password
        self._port = port
        self._path = "."

    def exit():
        raise NotImplementedError('subclass')

    def connect(self)->Result:
        raise NotImplementedError('subclass')

    def get_entries(self,path=".")->Result:
        raise NotImplementedError('subclass')

    def cd(self,path:str)->Result:
        raise NotImplementedError("subclass")

    def download_file(self,fname:str,save_path=".")->Result:
        raise NotImplementedError("subclass")

    def send_file(self,fname:str)->Result:
        raise NotImplementedError("subclass")
    
    @property
    def host(self):
        return self._host

    @property
    def user(self):
        return self._user

    @property
    def path(self):
        return self._path
