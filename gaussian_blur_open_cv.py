import cv2
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import itertools

np.random.seed(89)

img = cv2.imread('downloads/sunrise/8.220px-Little_Gasparilla_sunrise.jpg')

# Make this bigger to generate a dense grid
N = 3

# Create some random data
volume = np.random.rand(N, N, N) # 3 last dimensions to simulate the rgb

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

print(b)