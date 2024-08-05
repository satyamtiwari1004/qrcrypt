import eel
import webbrowser
import threading
import time

def start_eel():
    eel.init('web')
    eel.start('home.html', mode=False, block=False)  # Don't block so we can do other things
