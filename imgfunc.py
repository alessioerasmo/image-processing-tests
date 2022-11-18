import sys

def black_white(image):
    row = 0
    while (row<len(image)):
        column = 0
        while (column<len(image[row])):
            i = 0
            tot = 0
            while(i<3): 
                tot += image[row][column][i]
                i += 1
            average = tot/3
            i=0
            while (i<3):
                image[row][column][i] = average
                i+=1 
            column += 1
        row += 1         
    return image

def negative(image):
    row = 0
    while (row<len(image)):
        column = 0
        while (column<len(image[row])):
            i = 0
            while (i<3):
                image[row][column][i] = 255 - image[row][column][i] 
                i += 1
            column += 1
        row += 1    
    return image

def treshold(image, value):
    if (value < 0 | value > 255):
        raise Exception("insert a value between 0 and 255")
    row = 0
    while (row<len(image)):
        column = 0
        while (column<len(image[row])):
            i=0
            while (i<3):
                if (image[row][column][i]>value):
                    image[row][column][i] = 255
                else:
                    image[row][column][i] = 0
                i+=1 
            column += 1
        row += 1  
    return image