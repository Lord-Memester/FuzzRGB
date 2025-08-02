import random
import threading
import math
import time
import concurrent.futures
from PIL import Image, ImageDraw

start_time = time.monotonic()


# <editor-fold desc="User Input">
width = 1024 #int(input("Enter image width in pixels: "))
print(f"Width received: {width}")
height = 512 #int(input("Enter image height in pixels: "))
print(f"Height received: {height}")

# </editor-fold>
subdivisions = (math.floor(math.log2(height)))
print(f"Determined subdivisions for processing: {subdivisions}")

img = Image.new('RGBA', [width, height],(255,255,255, 255))
active_chunk_prev = 0
active_chunk = 1
def worker():
    subdivision1 = [height * math.floor(active_chunk_prev/subdivisions), height * math.floor(active_chunk/subdivisions)]
    ycoord = subdivision1[0]
    xcoord = 0
    while ( ycoord <= subdivision1[1] ):
        draw = ImageDraw.Draw(img)
        red = random.randrange(0,256,1)
        green = random.randrange(0,256,1)
        blue = random.randrange(0,256,1)
        alpha = 255 #random.randrange(0,256,1) #alpha value
        draw.point((xcoord,ycoord), fill=(red,green,blue,alpha))
        #print(f"R1: {red}, G1: {green}, B1: {blue}, A1: {alpha}")
        ycoord += 1
        if (ycoord == subdivision1[1]):
            xcoord += 1
            ycoord = 0
        if (xcoord == width):
            break

pool = concurrent.futures.ThreadPoolExecutor(max_workers=subdivisions)

i = 0
while i < subdivisions:
    pool.submit(worker)
    active_chunk_prev += 1
    active_chunk += 1
    i += 1

pool.shutdown(wait=True)


"""The idea here should be to split the generation into chunks. Whatever is the most acceptable factor less than or equal to twelve seems like a good target for the number of
chunks to be splitting up each column into."""

end_time = time.monotonic()
print(f"Duration: {end_time - start_time} s")

img.save("testV2.png") 