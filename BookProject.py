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
    arr_rotated = np.transpose(arr)
    return arr

def get_num(message_str, min_int, max_int):
    ''' Get a restricted numerical input from the user '''
    num = None
    while True:
        data = input(message_str)
        try:
            num = float(data)
            if num >= min_int and num <= max_int:
                break
            else:
                print("ERROR: Input must be between " + str(min_int) + " and " + str(max_int))
        except:
            print("ERROR: Input must be a number\n")
    return num

def get_book_data():
    img_data = get_image()
    height = get_num("Enter book height in inches\n")
    width = get_num("Enter book width in inches\n")
    num_pages = get_num("Enter number of pages in book\n")
    tolerance = get_num("Input a tolerance-threshold (0 - 255)\n"
                      "All values below this will not be considered part of the image\n")
    for i in img_data:
        print("Page " + i)
        get_page_cuts(img_data[1], tolerance)

def get_page_cuts(arr, tolerance):
    start = -1
    stop = -1
    cuts_list = []
    cut = []
    i = 0
    for elt in arr:
        if elt >= tolerance and start == -1:
            start = i
            cut.append(start)
            stop = -1
        elif elt < tolerance and start != -1 and stop == -1:
            stop = i
            cut.append(stop)
            cuts_list.append(cut)
            cut = []
            start = -1
        i += 1
    return cuts_list



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