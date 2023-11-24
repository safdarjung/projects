import cv2
import numpy as np

brdsize=int(input("brdsie: "))
numsq = int(input("numsq: "))
sqsize = int(brdsize/numsq)
red = (0,0,200)
black = (0,0,0)
nowcolor = black


while True:
    brd = np.zeros([brdsize,brdsize,3])
    for row in range(0,brdsize):
        for col in range(0,brdsize):
            brd[sqsize*row:sqsize*(row+1),sqsize*col:sqsize*(col+1)] = nowcolor
            if nowcolor==black:
                nowcolor=red
            else:
                nowcolor=black
        if nowcolor==black:

            nowcolor=red
        else:
            nowcolor=black
        

    cv2.imshow('mycheckboard',brd)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

