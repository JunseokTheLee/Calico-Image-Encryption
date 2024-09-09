from PIL import Image
import sys
import time
print("Welcome to ")
time.sleep(0.56)
print(r"""                                                                                                  
    ,o888888o.           .8.          8 8888          8 8888     ,o888888o.        ,o888888o.     
   8888     `88.        .888.         8 8888          8 8888    8888     `88.   . 8888     `88.   
,8 8888       `8.      :88888.        8 8888          8 8888 ,8 8888       `8. ,8 8888       `8b  
88 8888               . `88888.       8 8888          8 8888 88 8888           88 8888        `8b 
88 8888              .8. `88888.      8 8888          8 8888 88 8888           88 8888         88 
88 8888             .8`8. `88888.     8 8888          8 8888 88 8888           88 8888         88 
88 8888            .8' `8. `88888.    8 8888          8 8888 88 8888           88 8888        ,8P 
`8 8888       .8' .8'   `8. `88888.   8 8888          8 8888 `8 8888       .8' `8 8888       ,8P  
   8888     ,88' .888888888. `88888.  8 8888          8 8888    8888     ,88'   ` 8888     ,88'   
    `8888888P'  .8'       `8. `88888. 8 888888888888  8 8888     `8888888P'        `8888888P'     """)


time.sleep(0.1)
print("--------------------------------------------------------------------------------------------------------")
print("\n")

image = sys.argv

keys  = input("Input 16 total keys, separated by a space: 1-256 1-256 1-256 1-6 1-256 1-256 1-256 1-6 1-256 1-256 1-256 1-6 1-256 1-256 1-256 1-6: ")
time.sleep(0.1)
print("Request being processed. Please wait")
print("Request being processed. Please wait")
print("Request being processed. Please wait")
im = Image.open(image[1])
keys = keys.split()
colors = []

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
            c= (abs(abs(b[0] - a[0])  - abs(key[1] - key[2])),abs(abs(b[1] - a[1])- abs(key[0]  - key[2])), abs(abs(b[2] - a[2])- abs(key[0] - key[1])) )
            pixelsNew2[i,j] = c
    return img2
#WIP
def reverse_proc(im, key1, key2, key3, keyk):
    pixelMap = im.load()

    img = Image.new(im.mode, im.size)
    pixelsNew = img.load()

    img2 = Image.new(im.mode, im.size)
    pixelsNew2 = img2.load()

    def swapf_inverse(sizex, sizey, posx, posy, count):
        # Perform the reverse of the swapf operation
        for i in range(0 + posx, sizex // 2 + posx):
            for j in range(0 + posy, sizey // 2 + posy):
                a = pixelsNew[i, j]
                b = pixelsNew[i + sizex // 2, j]
                c = pixelsNew[i + sizex // 2, j + sizey // 2]
                d = pixelsNew[i, j + sizey // 2]

                pixelsNew[i, j] = d
                pixelsNew[i, j + sizey // 2] = c
                pixelsNew[i + sizex // 2, j + sizey // 2] = b
                pixelsNew[i + sizex // 2, j] = a

        if count == 2:
            return
        swapf_inverse(sizex // 2, sizey // 2, 0, 0, count + 1)
        swapf_inverse(sizex // 2, sizey // 2, sizex // 2, 0, count + 1)
        swapf_inverse(sizex // 2, sizey // 2, sizex // 2, sizey // 2, count + 1)
        swapf_inverse(sizex // 2, sizey // 2, 0, sizey // 2, count + 1)

    # Reverse the pixel manipulation based on the key order
    key = ()
    if keyk == 1:
        key = (key1, key2, key3)
    if keyk == 2:
        key = (key1, key3, key2)
    if keyk == 3:
        key = (key2, key1, key3)
    if keyk == 4:
        key = (key2, key3, key1)
    if keyk == 5:
        key = (key3, key1, key2)
    if keyk == 6:
        key = (key3, key2, key1)

    # Reverse the pixel manipulation process
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            a = pixelMap[i, j]
            b = pixelsNew[i, j]
            c = (
                abs(abs(b[0] + abs(key[1] - key[2])) - abs(a[0])),
                abs(abs(b[1] + abs(key[0] - key[2])) - abs(a[1])),
                abs(abs(b[2] + abs(key[0] - key[1])) - abs(a[2])),
            )
            pixelsNew2[i, j] = c

    swapf_inverse(img.size[0], img.size[1], 0, 0, 0)

    return img2

finalimage = proc(proc(proc(proc(im, int(keys[0]), int(keys[1]), int(keys[2]), int(keys[3])), int(keys[4]), int(keys[5]), int(keys[6]), int(keys[7])), int(keys[8]), int(keys[9]), int(keys[10]), int(keys[11])), int(keys[12]), int(keys[13]), int(keys[14]), int(keys[15]))
print("\n")
print("Done!")
time.sleep(0.2)
finalimage.show()


#125 229 99 3 200 150 190 2 56 231 111 4 103 42 250 5
