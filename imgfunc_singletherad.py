import sys
from numpy import *

def black_white(image):
    """
    Turns the image into a black and white one
    """
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
    """
    Turns the image into its negative 
    """
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
    """
    Set to the maximum intensity the rgb levels over the input value, 
    and set to 0 the others
    """
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

def bright(image, value):
    """
    Use it to brighten up the image of a value.
    the value is between 0 and 255 
    """
    if (value < 0 | value > 255):
        raise Exception("insert a value between 0 and 255")
    row = 0
    while (row<len(image)):
        column = 0
        while (column<len(image[row])):
            i = 0
            while(i<3): 
                if (image[row][column][i] <= (255-value)):
                    image[row][column][i] = image[row][column][i] + value
                else:
                    image[row][column][i] = 255
                i += 1
            column += 1
        row += 1  
    return image

def dark(image, value):
    """
    Decreases the brightness of the image by value.
    the value is between 0 and 255 
    """
    if (value < 0 | value > 255):
        raise Exception("insert a value between 0 and 255")
    row = 0
    while (row<len(image)):
        column = 0
        while (column<len(image[row])):
            i = 0
            while(i<3): 
                if (image[row][column][i] >= (0+value)):
                    image[row][column][i] = image[row][column][i] - value
                else:
                    image[row][column][i] = 0
                i += 1
            column += 1
        row += 1  
    return image

def random(image):
    """
    change colors with a random ones
    """
    from random import randint
    row = 0
    while (row<len(image)):
        column = 0
        while (column<len(image[row])):
            i = 0
            while(i<3): 
                image[row][column][i] = randint(0, 255)
                i += 1
            column += 1
        row += 1  
    return image

def blur(image, value):
    """
    blurs the image.
    the value parameter defines how heavy must be the blur effect
    """
    renderedimg = image.copy()
    row = 0
    while (row<len(image)):
        column = 0
        while (column<len(image[row])):
            i = 0
            while(i<3): 
                sum = 0
                values = 0
                k = -value
                while (k<value+1):
                    q = -value
                    while (q<value+1):
                        if ( ((row+k)>=0) & ((row+k)<len(image)) & ((column+q)>=0) & ((column+q)<len(image[row]))):
                            sum += image[row+k][column+q][i]    
                            values += 1
                        q +=  1
                    k += 1
                renderedimg[row][column][i]= int(sum/values)
                i += 1
            column += 1
        row += 1  
    return renderedimg

