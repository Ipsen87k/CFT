import paramiko
import json

# from ftp_client import FTPClient
# from sftp_client import SFTPClient
def get_user_pass()->list:
    arr = []
    with open('../ftppass.txt','r') as f:
        arr = [info for info in f.read().split(',')]

    return arr

def get_user_pass_privatekey()->list:
    with open('private.json','r',encoding='utf-8') as f:
        data = json.load(f)
    return [data.get('host'),data.get('user'),data.get('password'),data.get('privatekey')]

def main_t1():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    info = get_user_pass()
    try:
        client.connect(info[0],username=info[1],password=info[2])

        sftp_conn = client.open_sftp()
        files_info = sftp_conn.listdir_iter()

        [print(x.longname) for x in files_info]
    finally:
        sftp_conn.close()
        client.close()

import os
if __name__=='__main__':
    d = get_user_pass_privatekey()
    print(d)