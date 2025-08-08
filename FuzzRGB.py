import random
import os
import multiprocessing
import math
import time
import concurrent.futures
from PIL import Image, ImageDraw
print(f"Detected core count: {multiprocessing.cpu_count()}\n") #We get the number of cores to most make use of the multithreading, spreading the workload across all the CPU's cores as evenly as possible.

threads = multiprocessing.cpu_count()*2
i = 0
sequence_index = 0

print("Entries with integer values less than one will be automatically adjusted to a value of one.")
width = int(input("Enter image width in pixels: "))
if (width<=0): width=1
print(f"Width received: {width}")
height = int(input("Enter image height in pixels: "))
if (height<=0): height=1
print(f"Height received: {height}")

start_time = time.monotonic() #start overall timer


#subdivisions_x = (math.floor(math.log(width,threads)))
#if (subdivisions_x<=0): subdivisions_x=1
#subdivisions_y = (math.floor(math.log(height,threads)))
#if (subdivisions_y<=0): subdivisions_y=1

if (width > height):
    subdivisions = (math.floor(math.log(width,threads)))#subdivisions_x
    if (subdivisions<=0): subdivisions=1
elif (width < height):
    subdivisions = (math.floor(math.log(height,threads)))
    if (subdivisions<=0): subdivisions=1
elif (width == height):
    subdivisions = (math.floor(math.log(height,threads)))
    if (subdivisions<=0): subdivisions=1

#print(f"Determined subdivisions for processing: {subdivisions}")

img = Image.new('RGB', [width, height],(255,0,0)) #Image.new('RGBA', [width, height],(255,255,255, 255))

"""I believe more performance could be squeezed out of the program by generating 
the color of the pixels as a single decimal value that is then decoded into RGB(A) format.
It would allow the program to only calculate one random number per pixel. While the current
approach doesn't seem particularly resource-intensive, it would be an interesting
challenge and an intruiging experiment whether or not anything comes of it."""


#print("This text should appear once before worker_x")
def worker_x(): # used for landscape images
    active_subdivision_x = [math.floor(width * ((i-1)/(subdivisions))), math.floor(width * ((i)/(subdivisions)))]
    active_subdivision_start_x = active_subdivision_x[0]
    active_subdivision_end_x = active_subdivision_x[1]
    #print(f"active_subdivision_x = [math.floor((width={width}) * (((i={i}) - 1)/({subdivisions}))), math.floor(((width={width}) * (((i={i}))/({subdivisions})))]")
    thread_start_time = time.monotonic()
    print(f"Thread {i} running.\nactive_subdivision_start_x = {active_subdivision_start_x}\nactive_subdivision_end_x = {active_subdivision_end_x}\n")
    ycoord = 0
    xcoord = active_subdivision_start_x
    while ( xcoord <= active_subdivision_end_x ):
        draw = ImageDraw.Draw(img)
        red = random.randrange(0,256,1)
        green = random.randrange(0,256,1)
        blue = random.randrange(0,256,1)
        #alpha = 255 #random.randrange(0,256,1) #alpha value
        draw.point((xcoord,ycoord), fill=(red,green,blue)) #fill=(red,green,blue,alpha))
        #print(f"R1: {red}, G1: {green}, B1: {blue}, A1: {alpha}")
        xcoord += 1 # draw along columns
        if (xcoord == active_subdivision_end_x):
            ycoord += 1 # go to next row of pixels
            xcoord = 0 # start at beginning of the new row of pixels
        if (ycoord == height):
            break
    thread_end_time = time.monotonic()
    print(f"A \"columns-based\" thread finished after {thread_end_time - thread_start_time} seconds")
#print("This text should appear once after worker_x")

#print("This text should appear once before worker_y")
def worker_y(): # used for portrait (and square) images
    active_subdivision_y = [math.floor(height * ((i-1)/(subdivisions))), math.floor(height * ((i)/(subdivisions)))]
    active_subdivision_start_y = active_subdivision_y[0]
    active_subdivision_end_y = active_subdivision_y[1]
    #print(f"active_subdivision_y = [math.floor((height={height}) * (((i={i}) - 1)/({subdivisions}))), math.floor(((height={height}) * (((i={i}))/({subdivisions})))]")
    thread_start_time = time.monotonic()
    print(f"Thread {i} running.\nactive_subdivision_start_y = {active_subdivision_start_y}\nactive_subdivision_end_y = {active_subdivision_end_y}\n")
    ycoord = active_subdivision_start_y
    xcoord = 0
    while ( ycoord <= active_subdivision_end_y ):
        draw = ImageDraw.Draw(img)
        red = random.randrange(0,256,1)
        green = random.randrange(0,256,1)
        blue = random.randrange(0,256,1)
        #alpha = 255 #random.randrange(0,256,1) #alpha value
        draw.point((xcoord,ycoord), fill=(red,green,blue)) #fill=(red,green,blue,alpha))
        #print(f"R1: {red}, G1: {green}, B1: {blue}, A1: {alpha}")
        ycoord += 1 # draw along rows
        if (ycoord == active_subdivision_end_y):
            xcoord += 1 # go to next column of pixels
            ycoord = 0 # start at beginning of the new column of pixels
        if (xcoord == width):
            break
    thread_end_time = time.monotonic()
    print(f"A \"rows-based\" thread finished after {thread_end_time - thread_start_time} seconds")
#print("This text should appear once after worker_y")

pool = concurrent.futures.ThreadPoolExecutor(subdivisions)

while (i) < subdivisions:
    i +=1 # "i" is incremented to 1 before the workers ever run
    if (width > height):
        if (i==1): print("\nOptimizing processing for horizontal aspect ratio.\n") # "i" should only ever be 1 once, so this should only print once
        pool.submit(worker_x)
    elif (width < height):
        if (i==1): print("\nOptimizing processing for vertical aspect ratio.\n") # "i" should only ever be 1 once, so this should only print once
        pool.submit(worker_y)
    elif (width == height):
        if (i==1): print("\nThere is currently sub-optimal processing for the 1:1 aspect ratio. This might take a while.\n") # "i" should only ever be 1 once, so this should only print once
        pool.submit(worker_y)
"""I believe the way to truly optimize all processing would be to chop it into squares and do it a square at a time."""

pool.shutdown(wait=True)

end_time = time.monotonic()
print(f"\nAll threads completed!\nDuration: {end_time - start_time} seconds\n ")

img.save("random.png") 