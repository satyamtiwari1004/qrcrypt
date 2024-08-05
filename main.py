import io
import pyqrcode
from base64 import b64encode
import eel
import webbrowser
import threading
import time
import subprocess
from eelconfig import start_eel
from dropboxapi import TransferData
from encryption import Encryptor
import pyzbar
import os
import cv2
import requests

# Function to start the Eel server
def start_eel_thread():
    eel.init('web')
    eel.start('home.html', mode=False, block=False)  # Don't block so we can do other things

# Function to check if the Eel server is up
def is_server_running():
    url = 'http://localhost:8000/home.html'
    try:
        response = requests.get(url)
        print(response.status_code)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Function to open Brave browser in a new window
def open_browser():
    url = 'http://localhost:8000/home.html'
    # Wait until the server is running
    while not is_server_running():
        time.sleep(1)
    if os.name == 'nt':  # Windows
        subprocess.Popen(['start', 'brave', '--new-window', url], shell=True)
    elif os.name == 'posix':  # macOS and Linux
        subprocess.Popen(['open', '-a', 'Brave Browser', url])

# Start the Eel server and open the browser
threading.Thread(target=start_eel_thread).start()
open_browser()
# Object Creation
tdata = TransferData()
en = Encryptor()

@eel.expose
def generate_qr(data):
    try:
        data2 = en.encrypt_file(data)
        data1 = tdata.upload_file(data2)
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
            image = cv2.imread(data)
            barcodes = pyzbar.decode(image)
            for bar in barcodes:
                x, y, w, h = bar.rect
                bardata = bar.data.decode('utf-8')
                bartype = bar.type
            path1 = tdata.download_file(bardata)
            en.decrypt_file(path1)
            eel.success()
        else:
            eel.errr()
    except (SystemExit, MemoryError, KeyboardInterrupt):
        eel.errr()
