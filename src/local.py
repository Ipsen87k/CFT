import os
import data

def get_entry_type_from_path(path:str)->data.EntryType:
    if os.path.isfile(path):
        return data.EntryType.FILE
    elif os.path.isdir(path):
        return data.EntryType.DIR
    else:
        return data.EntryType.LINK

def main():
    for dirpath,dirnames,fnames in os.walk("."):
        print(dirpath)
        [print(f'directory {d}') for d in dirnames]
        [print(f'file {f}') for f in fnames]

main()