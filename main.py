import io
import pyqrcode
from base64 import b64encode
import eel
from test import TransferData
from script import Encryptor
from pyzbar import pyzbar
import os
import cv2
#Object Creation
tdata=TransferData()
en=Encryptor()

eel.init('web')




@eel.expose
def generate_qr(data):
    try:
        print("Hello")
        data2=en.encrypt_file(data)
        data1=tdata.upload_file(data2)
        img = pyqrcode.create(data1)
        buffers = io.BytesIO()
        img.png(buffers, scale=8)
        encoded = b64encode(buffers.getvalue()).decode("ascii")
        eel.success()
        return "data:image/png;base64, " + encoded
    except (SystemExit, MemoryError, KeyboardInterrupt):
        eel.errr()
@eel.expose
def read_qr(data):
    try:
        if os.path.exists(data):
            image=cv2.imread(data)
            barcodes=pyzbar.decode(image)
            for bar in barcodes:
                x,y,w,h=bar.rect
                bardata=bar.data.decode('utf-8')
                bartype=bar.type
            path1=tdata.download_file(bardata)
            en.decrypt_file(path1)
            eel.success()
        else:
            eel.errr()
    except (SystemExit, MemoryError, KeyboardInterrupt):
        eel.errr()





eel.start('home.html', size=(2700, 750))
