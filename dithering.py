from PIL import Image


im = Image.open("dog.jpg").convert('L')
pixels= im.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        pixels[i,j]=250
im.show()