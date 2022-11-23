import skimage
import math
from skimage import data, io

from imgfunc_miltitherad import *

# matplotlib usata per mostrare le immagini
import matplotlib.pyplot as plt
import matplotlib

image = io.imread("thumb-1920-1251351.jpg") # legge un'immagine
"""
    Restituisce una rappresentazione dell'immagine sotto forma 
    di array bidimesnionale, il cui valore di una singola cella 
    è un array contenente 3 valori (R G B)
"""

renderimg = black_white(image) 
print("execution time:")
print(duration)


plt.imshow(renderimg)
print("pixel processed: ")
print(len(image)*len(image[0]))


# io.imsave("out.png", renderimg )

plt.show()


"""
schiarisce l'immagine
i = 0
while(i<3): 
    if (image[column][row][i] <56):
        image[column][row][i] = image[column][row][i] + 200
    else:
        image[column][row][i] = 255
    i += 1

scurisce l'immagine
        i = 0
        while(i<3): 
            if (image[column][row][i] >200):
                image[column][row][i] = image[column][row][i] - 200
            else:
                image[column][row][i] = 0
            i += 1

bianco e nero
        i = 0
        tot = 0
        while(i<3): 
            tot += image[column][row][i]
            i += 1
        average = tot/3
        i=0
        while (i<3):
            image[column][row][i] = average
            i+=1  

negativo
        i = 0
        while (i<3):
            image[column][row][i] = 255 - image[column][row][i] 
            i += 1

bianco e nero + treshold 
        i = 0
        tot = 0
        while(i<3): 
            tot += image[column][row][i]
            i += 1
        average = tot/3
        i=0
        while (i<3):
            if (average>100):
                image[column][row][i] = 255
            else:
                image[column][row][i] = 0
            i+=1                            
"""

# print(len(image))