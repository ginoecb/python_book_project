import numpy as np
import scipy as sp
import scipy.ndimage as nd
import math
from PIL import Image

""" FUNCTIONS """
def get_image():
    ''' Retrieves specified image as a 2D array of greyscale pixels '''
    img_name = input("Enter filename of image\n"
                     "This image should be black-and-white only\n")
    img = Image.open(img_name)
    img_la = img.convert('L')
    arr = np.asarray(img_la)
    return arr

def get_book_info():

"""
testarr = get_image()
i = 0
while i < len(testarr):
    print(testarr[i])
    i += 1
"""

"""
print(len(arr[0]))          # height
print(len(arr[0][0]))       # width
print(len(arr[0][0][0]))    # RGB fields
"""