# _*_ coding= utf-8 _*_
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Image Denoising in OpenCV
fastNlMeansDenoisingColored(src[, dst[, h[, hColor[, templateWindowSize[, searchWindowSize]]]]]) → dst
Parameters:
•src – Input 8-bit 3-channel image.
•dst – Output image with the same size and type as src .
•templateWindowSize – Size in pixels of the template patch that is used to compute weights.
                    Should be odd. Recommended value 7 pixels
•searchWindowSize – Size in pixels of the window that is used to compute weighted average for
                    given pixel. Should be odd. Affect performance linearly:
                    greater searchWindowsSize - greater denoising time. Recommended value 21 pixels
•h – Parameter regulating filter strength for luminance component.
     Bigger h value perfectly removes noise but also removes image details,
     smaller h value preserves details but also preserves some noise
     (10 is ok)
•hForColorComponents – The same as h but for color components.
                    For most images value equals 10 will be enought to remove colored noise and
                    do not distort colors

"""
img = cv2.imread('./data/die.png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# One time
dst1 = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

# Two times
dst2 = cv2.fastNlMeansDenoisingColored(dst1, None, 10, 10, 7, 21)

plt.subplot(131), plt.imshow(img), plt.title('Origin')
plt.subplot(132), plt.imshow(dst1), plt.title('One Time')
plt.subplot(133), plt.imshow(dst2), plt.title('Two Times')
plt.show()
