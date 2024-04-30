from PIL import Image
import os, sys

path = "./Celeb Dataset"
dirs = os.listdir(path)

w = 255
h = 255

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((w, h), Image.ANTIALIAS)
            imResize.convert('RGB').save(f + '.jpg' + 'JPEG', quality=90)
