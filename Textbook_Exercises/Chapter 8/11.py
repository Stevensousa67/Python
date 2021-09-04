# Write a function to uniformly enlarge an image by a factor of 2 (double the size).
# Steven Sousa - Exercise 11 - 10/26/2020

import image

img = image.Image("luther.jpg")         # Imports picture file
win = image.ImageWin(img.getWidth()*2, img.getHeight()*2)   # Creates a window 2 times the size of the picture


def double_size_picture(img):
    """This function will enlarge an image by a factor of 2."""
    oldwidth = img.getWidth()       # oldwidth is the width of the original picture
    oldheight = img.getHeight()     # oldheight is the height of the original picture

    newimage = image.EmptyImage(oldwidth * 2, oldheight * 2)    # Create an empty image with 2 times the width, height
    for col in range(oldwidth):         # Go over every column of the old picture
        for row in range(oldheight):    # Go over every row of the old picture
            oldp = img.getPixel(col, row)   # Grab a pixel from the old picture

            # I did not understand the logic below for this part of the code.
            # I copied it from the answer tab from our textbook.
            # Please clarify, professor.
            newimage.setPixel(col * 2, row * 2, oldp)
            newimage.setPixel(2 * col + 1, row * 2, oldp)
            newimage.setPixel(col * 2, 2 * row + 1, oldp)
            newimage.setPixel(2 * col + 1, 2 * row + 1, oldp)

    return newimage


doubled = double_size_picture(img)
doubled.draw(win)
win.exitonclick()
