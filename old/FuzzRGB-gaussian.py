import random
import multiprocessing
import math
import time
import concurrent.futures
from PIL import Image, ImageDraw
print(f"Detected core count: {multiprocessing.cpu_count()}\n") #We get the number of cores to most make use of the multithreading, spreading the workload across all the CPU's cores as evenly as possible.

cores = multiprocessing.cpu_count()
i = 0
stdev = 35 # Trying to figure out how to match the histogram of this function to the uniform distribution of the old method may be an exercise in futility. Perhaps throwing things at the wall and seeing what sticks is not the ideal approach, and rather I should make use of the image library's filters to conform the histogram to be uniform, either with a 3D LUT or some other form of processing.

print("Entries with integer values less than one will be automatically adjusted to a value of one.")
width = int(input("Enter image width in pixels: "))
if (width<=0): width=1
print(f"Width received: {width}")
height = int(input("Enter image height in pixels: "))
if (height<=0): height=1
print(f"Height received: {height}")

start_time = time.monotonic() #start overall timer


if (width > height):
    subdivisions = (math.floor(math.log(width,cores)))#subdivisions_x
    if (subdivisions<=0): subdivisions=1
elif (width < height):
    subdivisions = (math.floor(math.log(height,cores)))
    if (subdivisions<=0): subdivisions=1
elif (width == height):
    subdivisions = (math.floor(math.log(height,cores)))
    if (subdivisions<=0): subdivisions=1
r = Image.effect_noise((width, height), stdev)
g = Image.effect_noise((width, height), stdev)
b = Image.effect_noise((width, height), stdev)
#a = Image.new("L",(width,height), 255)

img = Image.merge("RGB", (r, g, b ))

end_time = time.monotonic()
print(f"\nProcessing completed!\nDuration: {end_time - start_time} seconds\n ")

img = img.convert("RGB")

img.save("random-gaussian.png") 