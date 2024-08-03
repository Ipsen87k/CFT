import datetime
import pathlib

class Result:

    def __init__(self,value=None,err = None) -> None:
        self.value = value
        self.err = err

    def is_ok(self):
        if self.err is None and self.value:
            return True
        else:
            return False


    def is_err(self):
        if self.value is None and self.err:
            return True
        else:
            return False

    def ok(self):
        self.value = "ok"
        self.err = None
        return self

def path_join_slash(*path)->str:
    return "/".join(path)

def get_file_name(path:str)->str:
    return pathlib.Path(path).name



def write_error_log(func):
    def wrapper(*args,**kwargs):
        with open("../error.log",'a') as f:
            f.write("-----ERROR-----\n")
            f.write(f"{datetime.datetime.now()}\n")
            f.write(f"{str(args[0])}\n")
            #f.write(f"{str(err.with_traceback())}\n")
        return func(*args,**kwargs)

    return wrapper

##############
# qt_util    #
##############
from PySide6.QtWidgets import QMessageBox
@write_error_log
def error_dialog_show(err:Exception):
    dialog = QMessageBox()
    dialog.setWindowTitle("Error")
    dialog.setText(str(err))
    dialog.setIcon(QMessageBox.Icon.Critical)
    dialog.exec()


if __name__=='__main__':
    d = []
    print(len(d))
