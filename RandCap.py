import os
import time
from random import randint
from PIL import Image
count = 0
#Saves 100 images 
total = 100
while count<total:
    # captures the window
    os.system("import -window root screencap/temp.png")
    #generates a filename based on time
    filename = time.strftime("screencap/%Y%m%d%H%M%S.png")
    # Renames the temp.png to a time based filename Example:  20170911113012.png
    os.rename("screencap/temp.png", filename)
    print "Number : ",count+1,"of",total,"  FileName : ",filename
    # Adds a random timer
    nap = randint(60, 430)
    # Sleeps for the randomly chosen time
    time.sleep(nap)
    count = count +1

    