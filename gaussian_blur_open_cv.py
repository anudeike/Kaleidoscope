import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pictures/barcelona-morning-sky.jpg')

kernel_size = (45,45)
blur = cv2.GaussianBlur(img,kernel_size,0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()