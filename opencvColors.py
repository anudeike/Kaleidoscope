import cv2
import matplotlib.pyplot as plt
import numpy as np
from google_images_download import google_images_download # for webscrapping

# hyperparameters
blur_amt = 75 # for some reason only works in multiples of 5 that don't end in zero
result_count = 1 # amount of results we want
query = "sunrise"
format = "jpg" # will use jpg because they are smaller

# create function to retrieve the images
def getImagesFromGoogle(search_term, result_amt, pictureFormat, showURLs = True):

    #init the object from the lib
    response = google_images_download.googleimagesdownload()

    #arguments to pass into the download
    args = {
        "keywords": search_term,
        "format": pictureFormat,
        "limit": result_amt,
        "print_urls": showURLs
    }

    paths = ""
    # get the images
    try:
        paths = response.download(args)[0][search_term]
        print(paths)
    except FileNotFoundError:
        print("No files found for: " + str(search_term) + " in google image search.")

    # return the absolute paths to the images in the download folder
    return paths

def createHistogramFromSamplePictures(paths, blurAmount):
    # paths contain all the absolute paths to the images that the above code retrieved
    # define the kernel amount
    kernel_size = (blurAmount, blurAmount)
    color = ('b', 'g', 'r')
    # main forloop
    for path in paths:

        # create an img object and add the blur
        img = cv2.imread(path)
        blur = cv2.GaussianBlur(img, kernel_size, 0)

        #create the plot figure
        plt.subplot(211) #top
        plt.imshow(blur)

        # color values is a dictionary
        most_popular_color = {}

        for i, col in enumerate(color):
            histogram = cv2.calcHist([blur], [i], None, [256], [0, 256])

            # find the most popular color value
            max_val = max(histogram)
            max_index = np.where(histogram == max_val)
            most_popular_color[col] = max_index[0][0]

            #map the hex value
            plt.subplot(212)
            plt.plot(histogram, color = col)
            plt.xlim([0, 256])
            plt.xlabel("color value")
            plt.ylabel("frequencies")
            plt.title("")

        print(most_popular_color)
        plt.show() # show it just for now

    pass

# ===== FUNCTION DRIVER CODE ============#

#file_paths = getImagesFromGoogle(query, 1, format)
createHistogramFromSamplePictures(['downloads/sunrise/10.Haleakala_Sunrise_8.jpg'], 5)

# createHistogramFromSamplePictures(file_paths, 75)
# # this is the sample driver code
# file = "pictures/barcelona-morning-sky.jpg"
# img = cv2.imread(file)
#
#
# #blur the image using gaussaian blur
# kernel_size = (blur_amt, blur_amt)
# blur = cv2.GaussianBlur(img,kernel_size,0)
# color = ('b','g','r')
# plt.figure()
#
# #for each column and index in colors tuple
# for i, col in enumerate(color):
#     histogram = cv2.calcHist([blur], [i], None, [256], [0, 256])
#     plt.plot(histogram, color = col)
#     plt.xlim([0,256])
#     plt.xlabel("color value")
#     plt.ylabel("number of occurences")
#     plt.title(file[9:] + "-blur" + str(blur_amt))
#
# #save the file in the histogram folder
# save_path = "histograms/" + file[9:] + "-blur" + str(blur_amt) + "_hist.png"
# plt.savefig(save_path)
# plt.show()

