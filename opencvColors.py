import cv2
import matplotlib.pyplot as plt
import numpy as np

file = "pictures/barcelona-morning-sky.jpg"
img = cv2.imread(file)

blur_amt = 75 #only works in multples of five that don't end in 0

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

