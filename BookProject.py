import numpy as np
import sys
from PIL import Image

""" FUNCTIONS """
def get_image(img_name, height, num_pages):
    ''' Retrieves specified image as a 2D array of greyscale pixels '''
    img = Image.open(img_name)
    img_resized = img.resize((int(num_pages), int(height)), Image.NEAREST)
    img_resized.save(img_name[:-4] + "_resized" + img_name[-4:])
    img_la = img_resized.convert('L')
    arr = np.asarray(img_la)
    arr_rotated = np.transpose(arr)
    return arr_rotated

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

def get_page_cuts(arr, tolerance):
    ''' Determine cut distance(s) for a given page '''
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
    # If the entire page

    return cuts_list

def main():
    img_name = input("Enter filename of image\n"
                     "This image should be black-and-white only\n> ")
    height = get_num("Enter page height in inches\n> ", 0, sys.maxsize)
    num_pages = get_num("Enter number of pages in book\n> ", 0, sys.maxsize)
    tolerance = get_num("Input a tolerance-threshold (0 - 255)\n> "
                      "All values below this will not be considered part of the image\n> ", 0, 255)
    # 1 in : 96 px
    px_height = height * 96
    img_data = get_image(img_name, px_height, num_pages)
    outfile = open(img_name[:-4] + "_cut_instr.txt", "w")
    i = 0
    """for col in img_data:
        output = ""
        outstr = "Page " + str(i) + "\n"
        print(outstr)
        output += outstrx   
        cuts = get_page_cuts(img_data[1], tolerance)
        for cut in cuts:
            outstr = "Cut from " + str(cut[0] / px_height * height)\
                     + " in to " + str(cut[1] / px_height * height) + " in\n"
            print(outstr)
            output += outstr
        outfile.write(output)
        i += 1
    outfile.close()"""
    cuts = get_page_cuts(img_data[1], tolerance)
    print(cuts)
    for cut in cuts:
        print("From " + str(cut[0]) + " to " + str(cut[1]))

#main()

img = Image.open("testmat.png")
print(img.size)
img = img.convert('L')
arr = np.asarray(img)
#print(arr[0])
#arr = np.transpose(arr)
#print(arr[0])
i = 0
for col in arr:
    print(get_page_cuts(arr[i], 10))
    i += 1

'''
cuts = [9, 0, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 0]
cuts = get_page_cuts(cuts, 4)
for cut in cuts:
    print("From " + str(cut[0]) + " to " + str(cut[1]))
'''