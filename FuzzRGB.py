# I'm writing this in Python because I assume it's easier to look up libraries for.
import os, sys
from PIL import Image, ImageDraw
import random
import math

width = int(input("Enter image width in pixels: "))
print(f"Width received: {width}")
height = int(input("Enter image height in pixels: "))
print(f"Height received: {height}")

img = Image.new('RGBA', [width, height],(255,255,255, 255))

ycoord = 0
xcoord = 0
#numcolors = 3
#for x in width:
while (xcoord <= width ):
    draw = ImageDraw.Draw(img)
    rndnum = random.randrange(0,256,255)#(256/numcolors)-1)
    rndnum2 = random.randrange(0,256,255)#(256/numcolors)-1)
    rndnum3 = random.randrange(0,256,255)#(256/numcolors)-1)
    rndnum4 = 255 #random.randrange(0,256,255)#(256/numcolors)-1)#alpha value
    draw.point((xcoord,ycoord), fill=(rndnum,rndnum2,rndnum3,rndnum4))
    #print(rndnum,rndnum2,rndnum3,rndnum4)
    xcoord += 1
    if (xcoord == width):
        ycoord += 1
        xcoord = 0
    if (ycoord == height):
        break

img.save("test.png") #Epic B)
