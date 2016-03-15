# _*_ coding= utf-8 _*_

import numpy as np

a = np.arange(10) ** 3
print a

for i in a:
    print i**(1/3.)

a[:6:2] = -1000  # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
print a

print a[::-1]  # reversed a
