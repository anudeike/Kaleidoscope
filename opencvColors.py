import cv2
import matplotlib.pyplot as plt
import numpy as np
from google_images_download import google_images_download # for webscrapping
from mpl_toolkits.mplot3d import Axes3D
from skimage import io
import itertools


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

    # create a dictionary to hold most info about photos
    photos = []

    # main forloop
    for path in paths:
        # dictionary to hold paths and most popular color
        photo_info = {
            "path": path,
            "main_color": {

            }
        }

        # create an img object and add the blur
        img = cv2.imread(path)
        blur = cv2.GaussianBlur(img, kernel_size, 0)

        #create the plot figure
        # plt.subplot(211) #top
        # plt.imshow(blur)

        # color values is a dictionary
        most_popular_color = {}

        # for each color
        for i, col in enumerate(color):
            histogram = cv2.calcHist([blur], [i], None, [256], [0, 256])

            # find the most popular color value
            max_val = max(histogram)
            max_index = np.where(histogram == max_val)
            most_popular_color[col] = max_index[0][0]

            # #map the hex value
            # plt.subplot(212)
            # plt.plot(histogram, color = col)
            # plt.xlim([0, 256])
            # plt.xlabel("color value")
            # plt.ylabel("frequencies")
            # plt.title("")

        photo_info["main_color"] = most_popular_color # set the most popular color to this


        # append the photo info to the photos array
        photos.append(photo_info)

        #plt.show() # show it just for now

    # return the photos array
    return photos

def createPixelValueGraph(path):

    """
    :param path: path to file
    :return: displays a 3d graph that assumes
    """

    img = cv2.imread(path[0]) # get the image
    img = cv2.GaussianBlur(img, (5,5), 15)

    # get the height, width and channels of the img
    height, width, nchannels = img.shape
    print(height, width, nchannels)

    # double for loop to be able to get the entire 3d representation
    b = [] # for blue
    g = [] # for green
    r = [] # for red

    # print(img.size)
    print(img)

    r, g, b = [], [], []

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if k == 0:
                    b.append(img[i][j][k])
                if k == 1:
                    g.append(img[i][j][k])
                if k == 2:
                    r.append(img[i][j][k])

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.scatter(r, g, b, c=b)
    plt.show()
    pass

def createColorPaletteFromPictures(images_data, search_term):
    print(" createColorPaletteFunction ")

    palette = []
    for cell in images_data:
        c = list(cell["main_color"].values())
        c.reverse()
        palette.append(c)
    pal = np.asarray(palette)
    print("This is pal: ", pal)
    # palette
    indices = np.random.randint(0, len(palette), size=pal.shape)

    # show to the canvas
    io.imshow(pal[indices])

    # save the figure to a file
    plt.savefig("color_palette_test/palette_searchTerm-" + search_term + ".png")

    plt.show()

    pass
# ===== FUNCTION DRIVER CODE ============#

# get files from google
file_paths = getImagesFromGoogle(query, 5, format)

# create the histograms from the pictures
picture_data = createHistogramFromSamplePictures(file_paths, 5)

# create the color Palette
createColorPaletteFromPictures(images_data=picture_data, search_term=query)

# createPixelValueGraph(['downloads/sunset/beach.png'])

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

