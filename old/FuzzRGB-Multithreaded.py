# I'm writing this in Python because I assume it's easier to look up libraries for.
import os, sys
from PIL import Image, ImageDraw
import random
import math
import threading
import concurrent.futures
import time
import yappi

_NTHREAD = 2

start_time = time.monotonic_ns()

width = 512 #int(input("Enter image width in pixels: "))
print(f"Width received: {width}")
height = 512 #int(input("Enter image height in pixels: "))
print(f"Height received: {height}")

img = Image.new('RGBA', [width, height],(255,255,255, 255))

ycoord = 0
xcoord = 0
#numcolors = 3

#while (xcoord <= width ):
#    draw = ImageDraw.Draw(img)
#    rndnum1 = random.randrange(0,256,1)
#    rndnum2 = random.randrange(0,256,1)
#    rndnum3 = random.randrange(0,256,1)
#    rndnum4 = 255 #random.randrange(0,256,1) #alpha value
#    draw.point((xcoord,ycoord), fill=(rndnum1,rndnum2,rndnum3,rndnum4))
#    #print(rndnum,rndnum2,rndnum3,rndnum4)
#    xcoord += 1
#    if (xcoord == width):
#        ycoord += 1
#        xcoord = 0
#    if (ycoord == height):
#        break

def task1():
    subdivision1 = math.floor(width/2)
    x1coord = 0
    y1coord = 0
    while (x1coord <= subdivision1 ):
        draw = ImageDraw.Draw(img)
        rndnum1 = random.randrange(0,256,1)
        rndnum2 = random.randrange(0,256,1)
        rndnum3 = random.randrange(0,256,1)
        rndnum4 = 255 #random.randrange(0,256,1) #alpha value
        draw.point((x1coord,y1coord), fill=(rndnum1,rndnum2,rndnum3,rndnum4))
        #print(f"R1: {rndnum1}, G1: {rndnum2}, B1: {rndnum3}, A1: {rndnum4}")
        x1coord += 1
        if (x1coord == subdivision1):
            y1coord += 1
            x1coord = 0
        if (y1coord == height):
            break

def task2():
    time
    subdivision2 = math.ceil(width/2)
    x2coord = subdivision2
    y2coord = 0
    while ((x2coord) <= width):
        
        draw = ImageDraw.Draw(img)
        rndnum1 = random.randrange(0,256,1)
        rndnum2 = random.randrange(0,256,1)
        rndnum3 = random.randrange(0,256,1)
        rndnum4 = 255 #random.randrange(0,256,1) #alpha value
        draw.point((x2coord,y2coord), fill=(rndnum1,rndnum2,rndnum3,rndnum4))
        #print(f"R2: {rndnum1}, G2: {rndnum2}, B2: {rndnum3}, A2: {rndnum4}")
        x2coord += 1
        if (x2coord == width):
            y2coord += 1
            x2coord = subdivision2
        if (y2coord == height):
            #Time2 = time.process_time()
            break
            
    #img.save("test.png")


# I asked a friend, and they agreed that I could optimize this code with a combination of multithreading and by dividing processing into blocks.
# I should also implement a profiler to quantatively measure performance.

#blockSize = 4

if __name__ =="__main__":
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    end_time = time.monotonic_ns()
    print(f"Duration: {end_time - start_time} ns")

    img.save("test.png")

    #print(f"Thread 2: {Time2}")
    #print("Done!")













#img1.save("testp1.png") #Epic B)
#img2.save("testp2.png") #Epic B)