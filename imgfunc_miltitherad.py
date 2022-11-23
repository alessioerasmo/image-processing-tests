import multiprocessing
from threading import Thread
import time

corecount = multiprocessing.cpu_count()

def black_white(image):
    """
    Turns the image into a black and white one
    """

    to_divide = corecount
    processing_lines = len(image)
    lasting_lines = processing_lines%to_divide
    thread_handle = int((processing_lines-lasting_lines)/to_divide)

    

    print("rows: ")
    print(processing_lines)
    print("lines per thread: ")
    print(thread_handle)
    print("lasting lines to process: ")
    print(lasting_lines)


    

    i = 0
    while (i < processing_lines):
        if (i == 0):
            Thread(target=black_white_in, args=(image, i, (i + thread_handle + lasting_lines))).start() 
            i += lasting_lines    
        Thread(target=black_white_in, args=(image, i, (i + thread_handle))).start()
        i += thread_handle
    
  


    return image




def black_white_in(image, start, end):
    row = start
    while (row<end):
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
