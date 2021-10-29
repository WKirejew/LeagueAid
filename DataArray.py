import numpy, PIL, os
from PIL import Image
from numpy import asarray


def DataArray():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))            #ustawiamy obecny path na folder, w którym znajduje się plik .py
    img = Image.open('Klatka_next.png')
    macierz = asarray(img)
    return macierz
