import os
from PIL import Image
import random
import math
from bisect import bisect
from greyscale import scale, bounds
from download_image import download

def convert(url, filename):
    
    download(url, filename)
    
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(BASE_PATH, filename)
    im = Image.open(FILE_PATH)
    
    old_x = 1.2*im.size[0]
    old_y = im.size[1]
    
    a = 1.0
    b = 5.0*(old_y/old_x)
    c = (-40000.0*old_y) / old_x
    new_y = (-b + math.sqrt(pow(b, 2) - 4.0*a*c)) / (2.0*a)
    new_x = (new_y * old_x) / old_y
    
    size = math.floor(new_x), math.floor(new_y)
    #print(size)
    
    im = im.resize(size, Image.ANTIALIAS)
    im = im.convert("L")
    
    im.save('grayscale.jpg')
    
    out_str = ""
    
    for y in range(0, im.size[1]):
        out_str = out_str + "    "
        for x in range(0, im.size[0]):
            lum = 255 - im.getpixel((x,y))
            row = bisect(bounds, lum)
            possibles = scale[row-1]
            out_str = out_str+possibles[random.randint(0, len(possibles) - 1)]
        out_str = out_str + "\n"
        
    os.remove('grayscale.jpg')
    
    return out_str