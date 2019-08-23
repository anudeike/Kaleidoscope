import cv2
import matplotlib.pyplot as plt
import numpy as np

file = "pictures/barcelona-morning-sky.jpg"
img = cv2.imread(file)
color = ('b','g','r')
plt.figure()

#for each column and index in colors tuple
for i, col in enumerate(color):
    histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histogram, color = col)
    plt.xlim([0,256])
    plt.xlabel("color value")
    plt.ylabel("number of occurences")
    plt.title(file[9:])

#save the file in the histogram folder
save_path = "histograms/" + file[9:] + "_hist.png"
plt.savefig(save_path)
plt.show()

