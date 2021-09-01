
from PIL import Image

def binary(num):
    # each bit of message to 8bit binary
    # return list of bytes
    return [format(ord(i),"08b") for i in num]

def mod_pix_val(pix_val,data):
    # HEART OF ALGORITHM
    # modifies pixel values
    imdata=iter(pix_val)
    for i in range(len(data)):
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]
        for j in range(8):
            #for 1 in data  and pixel value even substract 1
            #for 0 in data  and pixel value odd substract 1
            if data[i][j]=='0' and pix[j]%2!=0:
                pix[j]-=1
            elif pix[j]%2==0 and data[i][j]=='1':
                if(pix[j]!=0):
                    pix[j]-=1
                else:
                    pix[j]+=1
        if (i == len(data) - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
 
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
        
        pix=tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encrypt(image,msg):
    # get width of image and then increment x coord until we reach rightmost edge of pic
    w,_=image.size
    binarymsg=binary(msg)
    (x,y)=(0,0)
    test=mod_pix_val(image.getdata(),binarymsg)
    
    for pixel in mod_pix_val(image.getdata(),binarymsg):
        print(type(pixel))
        if(x==w):
            x=0
            y+=1
        else:
            x+=1
def decode():
    #decrepyts the message from the image
    img = input("Enter image name(with extension) : ")

    image = Image.open(img, 'r')
 
    data = ''
    imgdata = iter(image.getdata())
 
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
 
        # string of binary data
        binstr = ''
    #if pixel value is odd insert 1 to binstring
    # for even value --->0 to binary string
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
 
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

    
# Driver Code
if __name__ == '__main__' :
    a = int(input("-----STAEGGGER-----".center(40),
                        "1. Encode\n2. Decode\n"))
    if (a == 1):
        path=input("enter the path of the image to")
        im = Image.open(path,'r')
        newimg=im.copy()
        secretmsg=input("secret message")
        encrypt(newimg,secretmsg)
        newimgname = input("Enter the name of new image(with extension) : ")
        newimg.save(newimgname, str(newimgname.split(".")[1].upper()))
    elif (a == 2):
        print("Decoded Word :  " + decode())

    #decode functon option  C:/Users/Hp/Pictures/Screenshots/testimg.png
    else:
        raise Exception("Enter correct input")