# Getting Started #
*bookFoldingAssistant.py* is used for Book Folding Art projects.
With this program, you can generate instructions for any image you would like to use.
Simply place a black and white image of the design you would like to fold into the book into the same directory as 
*bookFoldingAssistant.py*, take the required measurements listed below, and run the program. You will now have instructions for the lengths of the page which should be cut and folded to produce your desired design.

Run this with
```
python3 bookFoldingAssistant.py
```
Do note you will need to have *numpy* and either *PIL* or *Pillow* to use this program.

# Requirements #
To use this, you will need to provide:
- A black and white image of the desired design
- The height of the book in inches
- The number of pages in the book
     - If a page is numbered (different numbers on front and back), count it as a single page
     - Be sure to count non-numbered pages in both the front and back of the book
- The number of pages to offset the design from the front cover
- The number of pages to offset the design from the back cover
- A tolerance value (from 0 to 255)
     - Black pixels have a value of 0
     - White pixels have a value of 255
     - So any pixel whose value is less than the tolerance value will be considered part of the image, and therefore a fold

# Output #
Running the program will output the following:
- Cutting instructions, which are printed to the terminal and also saved as *filename_cut_instr.txt*
- A resized version of the original image, scaled to the dimensions of the book, which is saved as *filename_resized.png*

# Coming Soon #
- An option for generating instructions that involve folding only, no cutting
