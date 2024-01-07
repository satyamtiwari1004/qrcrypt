
import



# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024


# encrypt
with open("download.png", "rb") as fIn:
    with open("data.txt.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# get encrypted file size

"""f=open("data.txt.aes", "rb")
fout =f.read()
print(fout)
big_code = pyqrcode.create(fout, error='L', version=27, mode='binary')
big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()"""
