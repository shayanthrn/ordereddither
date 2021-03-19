from PIL import Image


im = Image.open("dog.jpg").convert('L')
orginal_pixels = im.load()
dithered_im=Image.new("L",(im.size[0]*2,im.size[1]*2),"black")
dithered_pixels = dithered_im.load()

# using [[0 2], as sliding window
#        [3 1]]

slidingwindow=[[0,2],[3,1]]

for i in range(im.size[0]):
    for j in range(im.size[1]):
        mappedvalue=orginal_pixels[i,j]/64     #maps 0-255 to [0-4)
        if(mappedvalue>slidingwindow[0][0]):   #check threshhold for index 0,0 of sliding window
            dithered_pixels[i*2,j*2]=255
        if(mappedvalue>slidingwindow[0][1]):   #check threshhold for index 0,1 of sliding window
            dithered_pixels[i*2,j*2+1]=255
        if(mappedvalue>slidingwindow[1][0]):   #check threshhold for index 1,0 of sliding window
            dithered_pixels[i*2+1,j*2]=255
        if(mappedvalue>slidingwindow[1][1]):   #check threshhold for index 1,1 of sliding window
            dithered_pixels[i*2+1,j*2+1]=255

dithered_im.show()
dithered_im.save("dithered.jpg")

