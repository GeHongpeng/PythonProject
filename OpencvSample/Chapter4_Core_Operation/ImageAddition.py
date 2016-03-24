# _*_ coding= utf-8 _*_

import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])

# Opencv: saturated operation
print cv2.add(x, y)  # 250+10 = 260 => 255

# Numpy: modulo operation
print x + y  # 250+10 = 260 % 256 = 4
