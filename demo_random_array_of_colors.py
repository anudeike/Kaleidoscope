import numpy as np
import matplotlib.pyplot as plt
from skimage import io


palette = np.array([[255, 0, 0],
                    [0, 255, 0],
                    [0, 0, 255]])

print(palette.shape)
indices = np.random.randint(0, len(palette), size=palette.shape)


io.imshow(palette[indices])
plt.show()