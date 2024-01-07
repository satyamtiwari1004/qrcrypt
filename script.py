import pyAesCrypt
import os
import os.path
from os import listdir
from os.path import isfile, join
from os import stat, remove
from test import TransferData

tdata=TransferData()
class Encryptor:
    def __init__(self):
        self.bufferSize = 64 * 1024
        self.password = "gXJQbLUMhzMjRqhTAQBdbpuPcKRPQA5bNYQ6QMa82VEsQhgEHfTUmRy9BNBhhwLS"
    def encrypt_file(self, file_name):
        try:
            with open(file_name, "rb") as fIn:
                pathen=file_name+ ".aes"
                with open(pathen, "wb") as fOut:
                    pyAesCrypt.encryptStream(fIn, fOut, self.password, self.bufferSize)
            return pathen
        except ValueError :
            os.remove(pathen)
    def decrypt_file(self, file_name):
        try:
            encFileSize = stat(file_name).st_size
            with open(file_name, "rb") as fIn:
                with open(file_name[:-4], "wb") as fOut:
                    pyAesCrypt.decryptStream(fIn, fOut, self.password, self.bufferSize, encFileSize)
            os.remove(file_name)
        except :
            pass
     



