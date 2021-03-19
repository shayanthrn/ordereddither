from PIL import Image
import sys
import numpy as np


def dithermatrix(size):
    #   [[0 2], base sliding window
    #    [3 1]]
    baseslidingwindow=np.matrix([[0,2],[3,1]])
    tempsize=4
    while(tempsize!=size**2):
        baseslidingwindow=np.block([[4*baseslidingwindow,4*baseslidingwindow+2],[4*baseslidingwindow+3,4*baseslidingwindow+1]])
        tempsize=baseslidingwindow.size
    return baseslidingwindow




name=input("please enter the image path:\n")
try:
    im = Image.open(name).convert('L')
except:
    print("not such a location")
    sys.exit(0)
orginal_pixels = im.load()
slidingwindowsize=int(input("please enter size of sliding window:(2,4,8,16,...)\n"))
if(slidingwindowsize%2!=0):
    print("not correct window size")
    sys.exit(0)
    
dithered_im=Image.new("L",(im.size[0]*slidingwindowsize,im.size[1]*slidingwindowsize),"black")
dithered_pixels = dithered_im.load()


slidingwindow=dithermatrix(slidingwindowsize)

for i in range(im.size[0]):
    for j in range(im.size[1]):
        mappedvalue=orginal_pixels[i,j]/64     #maps 0-255 to [0-4)
        for k in range(slidingwindowsize):
            for p in range(slidingwindowsize):
                if(mappedvalue>slidingwindow[k,p]):   #check threshhold for index k,p of sliding window
                    dithered_pixels[i*slidingwindowsize+k,j*slidingwindowsize+p]=255

dithered_im.show()
dithered_im.save("dithered.jpg")

