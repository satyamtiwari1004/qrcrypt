import pyAesCrypt
import pyqrcode
from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = ""

# encrypt
with open("data.txt", "rb") as fIn:
    with open("data.txt.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# get encrypted file size
encFileSize = stat("data.txt.aes").st_size
print(encFileSize)

with open("data.txt.aes", "rb") as fIn:
    try:
        with open("dataout.txt", "wb") as fOut:
            # decrypt file stream
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
    except ValueError:
        # remove output file on error
        remove("dataout.txt")
"""f=open("data.txt.aes", "rb")
fout =f.read()
print(fout)
big_code = pyqrcode.create(fout, error='L', version=27, mode='binary')
big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()"""
