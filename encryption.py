from PIL import Image
im = Image.open('asdf.jpeg')



def proc(im, key1, key2, key3, keyk):
    pixelMap = im.load()

    img = Image.new( im.mode, im.size)
    pixelsNew = img.load()

    img2 = Image.new(im.mode, im.size)
    pixelsNew2 = img2.load()

    

    def swapf(sizex, sizey, posx, posy, count):

    
        for i in range(0 + posx, sizex//2 + posx):
            for j in range(0 + posy, sizey//2 + posy):
                a = pixelsNew[i,j]
                b= pixelsNew[i+sizex//2,j]
                c = pixelsNew[i+sizex//2, j + sizey//2]
                d = pixelsNew[i, j+sizey//2]

                pixelsNew[i+sizex//2,j] = a
                pixelsNew[i+sizex//2, j + sizey//2] = b
                pixelsNew[i, j+sizey//2] = c
                pixelsNew[i,j] = d
        
        if (count == 2):
            return
        swapf(sizex//2, sizey//2, 0, 0, count + 1)
        swapf(sizex//2, sizey//2, sizex//2, 0, count + 1)
        swapf(sizex//2, sizey//2, sizex//2, sizey//2, count + 1)
        swapf(sizex//2, sizey//2, 0, sizey//2, count + 1)

    


    for i in range(img.size[0]):
        for j in range(img.size[1]):
            
            pixelsNew[i,j] = pixelMap[i,j]

    key = ()
    if (keyk == 1):
        key = (key1, key2, key3)
    if (keyk == 2):
        key = (key1, key3, key2)
    if (keyk == 3):
        key = (key2, key1, key3)
    if (keyk== 4):
        key = (key2, key3, key1)
    if (keyk == 5):
        key = (key3, key1, key2)
    if (keyk == 6):
        key = (key3, key2, key1)


    swapf(img.size[0], img.size[1], 0, 0, 0)

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            a = pixelsNew[i, j]
            b= pixelMap[i,j]
            c= ((b[0] + a[0]) + key[0] - key[1] - key[2],b[1] + a[1]- key[0] + key[1] - key[2], (b[2] + a[2])- key[0] - key[1] + key[2])
            
    return img2



proc(proc(im, 125, 229, 456, 3), 256, 333, 425, 2).show()