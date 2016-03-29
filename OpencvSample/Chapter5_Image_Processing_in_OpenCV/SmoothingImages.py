# _*_ coding= utf-8 _*_
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
2D Convolution ( Image Filtering )
Python: Filter2D(src, ddepth, kernel, anchor=(-1, -1))
ddepth –
desired depth of the destination image; if it is negative, it will be the same as src.depth()
when ddepth=-1, the output image will have the same depth as the source.
"""
img = cv2.imread('./data/logo.png')

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


"""
1. Averaging
blur(src, ksize[, dst[, anchor[, borderType]]]) → dst
Parameters:
src – input image; it can have any number of channels, which are processed independently,
      but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst – output image of the same size and type as src.
ksize – blurring kernel size.
anchor – anchor point; default value Point(-1,-1) means that the anchor is at the kernel center.
borderType – border mode used to extrapolate pixels outside of the image.

boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) → dst
Parameters:
src – input image.
dst – output image of the same size and type as src.
ddepth – the output image depth (-1 to use src.depth()).
ksize – blurring kernel size.
anchor – anchor point; default value Point(-1,-1) means that the anchor is at the kernel center.
normalize – flag, specifying whether the kernel is normalized by its area or not.
borderType – border mode used to extrapolate pixels outside of the image.
If you don’t want to use a normalized box filter,
use cv2.boxFilter() and pass the argument normalize=False to the function.
"""
img = cv2.imread('./data/logo.png')

blur = cv2.blur(img, (5, 5))

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

"""
2. Gaussian Filtering
GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) → dst
Parameters:
src – input image; the image can have any number of channels, which are processed independently,
      but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst – output image of the same size and type as src.
ksize – Gaussian kernel size. ksize.width and ksize.
        height can differ but they both must be positive and odd.
        Or, they can be zero’s and then they are computed from sigma* .
sigmaX – Gaussian kernel standard deviation in X direction.
sigmaY – Gaussian kernel standard deviation in Y direction;
         if sigmaY is zero, it is set to be equal to sigmaX, if both sigmas are zeros,
        they are computed from ksize.width and ksize.height ,
        respectively (see getGaussianKernel() for details);
        to fully control the result regardless of possible future modifications of all this semantics,
        it is recommended to specify all of ksize, sigmaX, and sigmaY.
borderType – pixel extrapolation method (see borderInterpolate() for details).

getGaussianKernel(ksize, sigma[, ktype]) → retval
Parameters:
ksize – Aperture size. It should be odd ( \texttt{ksize} \mod 2 = 1 ) and positive.
sigma – Gaussian standard deviation. If it is non-positive,
        it is computed from ksize as sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8 .
ktype – Type of filter coefficients. It can be CV_32f or CV_64F
"""
img = cv2.imread('./data/logo.png')

blur = cv2.GaussianBlur(img, (5, 5), 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Gaussian blurring')
plt.xticks([]), plt.yticks([])
plt.show()
