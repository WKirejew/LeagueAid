import PIL, os
from PIL import Image, ImageGrab
from numpy import asarray

def ScreenShot():
    ss = ImageGrab.grab()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))            #ustawiamy obecny path na folder, w którym znajduje się plik .py
    ss.save("Klatka_next.png")
    return ss