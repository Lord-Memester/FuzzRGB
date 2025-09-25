import numpy as np
from numpy.random import default_rng
import time
from PIL import Image


print("Entries with integer values less than one will be automatically adjusted to a value of one.")
width = int(input("Enter image width in pixels: "))
if (width<=0): width=1
print(f"Width received: {width}")
height = int(input("Enter image height in pixels: "))
if (height<=0): height=1
print(f"Height received: {height}")

start_time = time.monotonic() #start performance timer

randarray = np.ceil((255*(default_rng().random((height, width, 3))))) # order of axes is (height, width, depth). In this use case, depth is the number of color channels.

# Next step is to map the floats generated in the array such that 0.0 is 0 and 1.0 is 255. 
# The floats generated within the array are a half-open interval, so values of 0.0 could be generated but values of 1.0 WILL NOT be generated. 
# Accordingly, rounding of some sort will be needed to reach the full range of 24-bit color values. Update: did the mapping and rounding within the creation of the array.

img_r = Image.fromarray(randarray[0:(height+1), 0:(width+1), 0]).convert("L") # red channel
img_g = Image.fromarray(randarray[0:(height+1), 0:(width+1), 1]).convert("L") # green channel
img_b = Image.fromarray(randarray[0:(height+1), 0:(width+1), 2]).convert("L") # blue channel

img = Image.merge("RGB", (img_r, img_g, img_b)) # math is so cool :3

end_time = time.monotonic() # end performance timer

print(f"\nAll processing completed!\nDuration: {end_time - start_time} seconds\n ")

img.save("random.png") 
