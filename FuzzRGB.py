# I'm writing this in Python because I assume it's easier to look up libraries for.
import os, sys
from PIL import Image, ImageDraw
import random

img = Image.new('RGB', [512, 512],(255,255,255))
#alright so that's correct but i don't know if it's actually generating an image file. I don't think it is.
#img.save("test.jpg")
#hey that works, cool! now I have to figure out how to color specific pixels of the image.

#draw = ImageDraw.Draw(img)
#draw.point((0,0), fill=0)
# i'm gonna try just moving the save statement down here to see if it prevents me from needing to modify the file, since that feels like it would be innefficient


#alright that also worked but the picture looks wrong and noisy where that pixel is. Maybe PNG would fix it? | Answer: Yes! very cool. Also, PNG supports transparency, which isn't in use (yet) but could be useful later.
#I'll probably need a for loop that goes over each pixel of the image and randomizes it. There's probably a FAR better way to make the pixels random but I don't know how yet.

#Now I will have to determine how one writes a for loop in python

#I also need to determine how to get user input and use that to set variables. Maybe look at some of my old C++ code from class to recall how to increment an integer up to a limit.

ycoord = 0
xcoord = 0
width = 512
height = 512
#for x in width:
while (xcoord <= width ):
    draw = ImageDraw.Draw(img)
    rndnum = random.randrange(255)
    rndnum2 = random.randrange(255)
    rndnum3 = random.randrange(255)
    draw.point((xcoord,ycoord), fill=(rndnum,rndnum2,rndnum3))
    xcoord += 1
    if (xcoord == width):
        ycoord += 1
        xcoord = 0
    if (ycoord == height):
        break

img.save("test2.png") #OH MY GOD I DID IT I'M SO PROUD OF MYSELF 