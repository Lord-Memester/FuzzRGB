import random
import threading
import multiprocessing
import math
import time
import concurrent.futures
from PIL import Image, ImageDraw
print(f"Detected core count: {multiprocessing.cpu_count()}\n") #We get the number of cores to most make use of the multithreading, spreading the workload across all the CPU's cores as evenly as possible.

i = 0

print("Entries with integer values less than one will be automatically adjusted to a value of one.")
width = int(input("Enter image width in pixels: "))
if (width<=0): width=1
print(f"Width received: {width}")
height = int(input("Enter image height in pixels: "))
if (height<=0): height=1
print(f"Height received: {height}")

start_time = time.monotonic() #start overall timer


subdivisions_x = (math.floor(math.log(width,multiprocessing.cpu_count())))
if (subdivisions_x<=0): subdivisions_x=1
subdivisions_y = (math.floor(math.log(height,multiprocessing.cpu_count())))
if (subdivisions_y<=0): subdivisions_y=1

if (width > height):
    subdivisions = subdivisions_x
elif (width <= height):
    subdivisions = subdivisions_y


img = Image.new('RGB', [width, height],(255,0,0)) #Image.new('RGBA', [width, height],(255,255,255, 255))

"""I believe more performance could be squeezed out of the program by generating 
the color of the pixels as a single decimal value that is then decoded into RGB(A) format.
It would allow the program to only calculate one random number per pixel. While the current
approach doesn't seem particularly resource-intensive, it would be an interesting
challenge and an intruiging experiment whether or not anything comes of it."""

def worker_x(): # used for landscape images
    print(f"Determined subdivisions_x for processing: {subdivisions_x}")
    active_subdivision_x = [math.floor(width * ((i-1)/(subdivisions_x))), math.floor(width * ((i)/(subdivisions_x)))]
    active_subdivision_start_x = active_subdivision_x[0]
    active_subdivision_end_x = active_subdivision_x[1]
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
        xcoord += 1
        if (xcoord == active_subdivision_end_x):
            ycoord += 1
            xcoord = 0
        if (ycoord == height):
            break
        thread_end_time = time.monotonic()
    print(f"A \"columns-based\" thread finished after {thread_end_time - thread_start_time} seconds")

def worker_y(): # used for portrait (and square) images
    print(f"Determined subdivisions_y for processing: {subdivisions_y}")
    active_subdivision_y = [math.floor(height * ((i-1)/(subdivisions_y))), math.floor(height * ((i)/(subdivisions_y)))]
    active_subdivision_start_y = active_subdivision_y[0]
    active_subdivision_end_y = active_subdivision_y[1]
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
        ycoord += 1
        if (ycoord == active_subdivision_end_y):
            xcoord += 1
            ycoord = 0
        if (xcoord == width):
            break
    thread_end_time = time.monotonic()
    print(f"A \"rows-based\" thread finished after {thread_end_time - thread_start_time} seconds")


pool = concurrent.futures.ThreadPoolExecutor(subdivisions_x)
pool = concurrent.futures.ThreadPoolExecutor(subdivisions_y)

while (i) < subdivisions:
    i +=1
    if (width > height):
        if (i==1): print("\nOptimizing processing for horizontal aspect ratio.\n")
        pool.submit(worker_x)
    elif (width < height):
        if (i==1): print("\nOptimizing processing for vertical aspect ratio.\n")
        pool.submit(worker_y)
    elif (width == height):
        if (i==1): print("\nThere is currently sub-optimal processing for the 1:1 aspect ratio. This might take a while.\n")
        pool.submit(worker_y)
"""I believe the way to truly optimize all processing would be to chop it into squares and do it a square at a time."""

pool.shutdown(wait=True)

end_time = time.monotonic()
print(f"\nAll threads completed!\nDuration: {end_time - start_time} seconds\n ")

img.save("random.png") 