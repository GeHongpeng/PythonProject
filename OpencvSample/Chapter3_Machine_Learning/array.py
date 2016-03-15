# _*_ coding= utf-8 _*_
#一维 数组可以被索引、切片和迭代
import numpy as np

a = np.arange(10) ** 3
print a

for i in a:
    print i**(1/3.)

a[:6:2] = -1000  # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
print a

print a[::-1]  # reversed a

# 多维 数组可以每个轴有一个索引
def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
print b

print b[0:5, 1]  # each row in the second column of b

print b[:, 1]  # equivalent to the previous example

print b[1:3]  # each column in the second and third row of b

print b[1:3, :]  # equivalent to the previous example

print b[-1]  # the last row. Equivalent to b[-1,:]

# 更改数组的形状
a = np.floor(10 * np.random.random((3, 4)))
print a
print a.shape
print a.ravel()  # flatten the array

a.shape = (6, 2)
print a
print a.transpose()  # Permute the dimensions of an array
