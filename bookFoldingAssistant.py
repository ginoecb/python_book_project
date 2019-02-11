import numpy as np
import sys
from PIL import Image

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

def get_page_cuts(arr, min_cut_len, tolerance, px_height, height):
    ''' Determine cut distance(s) for a given page '''
    start_cut = True
    cuts = []
    for idx, elt in enumerate(arr):
        if elt < tolerance and start_cut:
            cuts.append(idx)
            start_cut = False
        elif elt >= tolerance and not start_cut:
            cuts.append(idx)
            start_cut = True
            cuts = check_page_cuts(cuts, min_cut_len, px_height, height)
    if not start_cut:
        cuts.append(len(arr))
    return cuts

def check_page_cuts(cuts, min_cut_len, px_height, height):
    ''' Removes cut instructions if less than minimum cut length '''
    end = len(cuts) - 1
    if get_height(cuts[end] - cuts[end - 1], px_height, height) < min_cut_len:
        cuts = cuts[:-2]
    return cuts

def get_height(num, px_height, height):
    ''' Converts from pixel to inches '''
    return round(num / px_height * height, 4)

def main():
    ''' Calculates book measurements, saves Instructions and Resized image '''
    img_name = input("Enter filename of image\n"
                     "This image should be black-and-white only\n> ")
    height = get_num("Enter page height in inches\n> ", 0, sys.maxsize)
    num_pages = get_num("Enter number of pages in book\n"
                        "Numbered pages (with different numbers on front and back) will count as a signle page\n"
                        "Be sure to include non-numbered pages\n> ", 0, sys.maxsize)
    offset_front = get_num("Enter number of pages to offset image from the front cover\n> ", 0, num_pages)
    offset_back = get_num("Enter number of pages to offset image from the back cover\n> ", 0, num_pages)
    min_cut_len = get_num("Enter the minimum cut length in inches for each page\n> ", 0, height)
    tolerance = get_num("Input a tolerance-threshold (0 - 255)\n"
                      "All values above this will not be considered part of the image\n> ", 0, 255)
    width = num_pages - offset_front - offset_back
    # 1 in : 96 px
    px_height = height * 96
    img_data = get_image(img_name, px_height, width)
    outfile = open(img_name[:-4] + "_cut_instr.txt", "w")
    output = ""
    for idx, elt in enumerate(img_data):
        output += "\nPage " + str(int(idx + 1 + offset_front)) + "\n"
        cuts = get_page_cuts(img_data[idx], min_cut_len, tolerance, px_height, height)
        start_cut = True
        no_instr = True
        for num in cuts:
            if start_cut:
                no_instr = False
                output += "Cut from " + str(get_height(num, px_height, height)) + " in "
                start_cut = False
            else:
                output += "to " + str(get_height(num, px_height, height)) + " in\n"
                start_cut = True
        if no_instr:
            output += "None\n"
    print(output)
    outfile.write(output)
    outfile.close()

main()
