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
plt.subplot(122), plt.imshow(blur), plt.title('Averaging Filtering')
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
plt.subplot(122), plt.imshow(blur), plt.title('Gaussian Filtering')
plt.xticks([]), plt.yticks([])
plt.show()


"""
3. Median Filtering
medianBlur(src, ksize[, dst]) → dst
Parameters:
src – input 1-, 3-, or 4-channel image; when ksize is 3 or 5, the image depth should be CV_8U, CV_16U,
      or CV_32F, for larger aperture sizes, it can only be CV_8U.
dst – destination array of the same size and type as src.
ksize – aperture linear size; it must be odd and greater than 1, for example: 3, 5, 7 ...

"""
def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0] = 255
            img[j, i, 1] = 255
            img[j, i, 2] = 255
    return img

img = cv2.imread('./data/logo.png')
salt_img = salt(img, 500)

median = cv2.medianBlur(salt_img, 5)

plt.subplot(121), plt.imshow(salt_img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median), plt.title('Median Filtering')
plt.xticks([]), plt.yticks([])
plt.show()


"""
4. Bilateral Filtering
bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) → dst
Parameters:
src – Source 8-bit or floating-point, 1-channel or 3-channel image.
dst – Destination image of the same size and type as src .
d – Diameter of each pixel neighborhood that is used during filtering.
    If it is non-positive, it is computed from sigmaSpace .
sigmaColor – Filter sigma in the color space. A larger value of the parameter means that
             farther colors within the pixel neighborhood (see sigmaSpace ) will be mixed together,
             resulting in larger areas of semi-equal color.
sigmaSpace – Filter sigma in the coordinate space. A larger value of the parameter means that farther
             pixels will influence each other as long as their colors are close enough
             (see sigmaColor). When d>0 , it specifies the neighborhood size regardless of sigmaSpace.
             Otherwise, d is proportional to sigmaSpace .

"""
img = cv2.imread('./data/logo.png')

bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)
adaptiveBilateralFilter = cv2.adaptiveBilateralFilter(img, (9, 9), 75, 75)

plt.subplot(131), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(bilateralFilter), plt.title('Bilateral Filtering')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(adaptiveBilateralFilter), plt.title('Ada Bilateral Filtering')
plt.xticks([]), plt.yticks([])
plt.show()
