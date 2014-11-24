import os
import urllib

def download(url, filename):
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(BASE_PATH, filename)
    
    urllib.urlretrieve(url, FILE_PATH)