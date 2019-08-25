import cv2
import matplotlib.pyplot as plt
import numpy as np
from google_images_download import google_images_download # for webscrapping

# hyperparameters
blur_amt = 75 # for some reason only works in multiples of 5 that don't end in zero
result_count = 1 # amount of results we want
query = "sunset"
format = "jpg" # will use jpg because they are smaller


#initialize the class
resp = google_images_download.googleimagesdownload()

# create the arguments to pass in
arg = {
    "keywords": query,
    "format": format,
    "limit": result_count,
    "print_urls": True
}

# get the download
try:
    paths = resp.download(arg)[0][query] # should return the absolute paths of the images that were collected
    print(paths)
except FileNotFoundError:
    print("files not found")

def createHistogramFromSamplePictures(paths, blurAmount):
    # paths contain all the absolute paths to the images that the above code retrieved
    # define the kernel amount
    kernel_size = (blurAmount, blurAmount)
    color = ('b', 'g', 'r')
    # main forloop
    for path in paths:

        # create an img object and add the blur
        img = cv2.imread(path)
        cv2.GaussianBlur(img, kernel_size, 0)

        #create the plot figure
        plt.figure()

        for i, col in enumerate(color):
            histogram = cv2.calcHist([blur], [i], None, [256], [0, 256])
            plt.plot(histogram, color = col)
            plt.xlim([0, 256])
            plt.xlabel("color value")
            plt.ylabel("frequencies")
            plt.title("")

    pass

file = "pictures/barcelona-morning-sky.jpg"
img = cv2.imread(file)


#blur the image using gaussaian blur
kernel_size = (blur_amt, blur_amt)
blur = cv2.GaussianBlur(img,kernel_size,0)
color = ('b','g','r')
plt.figure()

#for each column and index in colors tuple
for i, col in enumerate(color):
    histogram = cv2.calcHist([blur], [i], None, [256], [0, 256])
    plt.plot(histogram, color = col)
    plt.xlim([0,256])
    plt.xlabel("color value")
    plt.ylabel("number of occurences")
    plt.title(file[9:] + "-blur" + str(blur_amt))

#save the file in the histogram folder
save_path = "histograms/" + file[9:] + "-blur" + str(blur_amt) + "_hist.png"
plt.savefig(save_path)
plt.show()

