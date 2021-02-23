'''
3.10 矩阵与线性代数运算
问题
你需要执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组等
等。
解决方案
NumPy 库有一个矩阵对象可以用来解决这个问题。
'''
import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)
print(m.T)
print(m.I)

'''
可以在numpy.linalg 子包中找到更多的操作函数
'''
import numpy.linalg
print(numpy.linalg.det(m))
print(numpy.linalg.eigvals(m))
# x = numpy.linalg.solve(m, v)
# print(x)