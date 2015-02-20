import os
from PIL import Image
import random
import math
from bisect import bisect
from greyscale import scale, bounds
#from download_image import download

def convert(filename, N = 100000, write=False):
    
    #filename, headers = download(url)
    
    #BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    #FILE_PATH = os.path.join(BASE_PATH, filename)
    im = Image.open(filename)
    
    x_scaling = 1.2
    old_x = x_scaling*im.size[0]
    old_y = im.size[1]
    
    #a = 1.0
    #b = 5.0*(old_y/old_x)
    #c = (-40000.0*old_y) / old_x
    #new_y = (-b + math.sqrt(pow(b, 2) - 4.0*a*c)) / (2.0*a)
    #N = 100000;
    new_y = math.sqrt((old_y*N)/old_x)
    new_x = (new_y * old_x) / old_y
    
    size = math.floor(new_x), math.floor(new_y)
    
    im = im.resize(size, Image.ANTIALIAS)
    im = im.convert("L")
    
    out_str = ""
    
    for y in range(0, im.size[1]):
        for x in range(0, im.size[0]):
            lum = 255 - im.getpixel((x,y))
            row = bisect(bounds, lum)
            possibles = scale[row-1]
            out_str = out_str+possibles[random.randint(0, len(possibles) - 1)]
        out_str = out_str + "\n"
    
    #os.remove(FILE_PATH)

    if write:
        with open(filename + ".txt", 'w') as f:
            f.write(out_str)
    
    return out_str