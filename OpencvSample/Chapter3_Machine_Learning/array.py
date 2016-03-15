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
# 如果在改变形状操作中一个维度被给做-1，其维度将自动被计算
a = np.floor(10 * np.random.random((3, 4)))
print a
print a.shape
print a.ravel()  # flatten the array

a.shape = (6, 2)
print a
print a.transpose()  # Permute the dimensions of an array


# 组合(stack)不同的数组
# 几种方法可以沿不同轴将数组堆叠在一起：
a = np.floor(10 * np.random.random((2, 2)))
print a

b = np.floor(10 * np.random.random((2, 2)))
print b

print np.vstack((a, b))
print np.hstack((a, b))

# 函数 column_stack 以列将一维数组合成二维数组，它等同与 vstack 对一维数组。
print np.column_stack((a, b)), '\n'


a = np.array([1., 2.])
b = np.array([3., 4.])
print a
print b

print a[:, np.newaxis]  # This allows to have a 2D columns vector
print b[:, np.newaxis]

print np.column_stack((a[:, np.newaxis], b[:, np.newaxis]))
print np.vstack((a[:, np.newaxis], b[:, np.newaxis]))  # The behavior of vstack is different

# 对那些维度比二维更高的数组， hstack 沿着第二个轴组合， vstack 沿着第一个轴组合, concatenate 允许可选参数给出组合时沿着的轴。

print np.r_[1:4, 0, 4]
