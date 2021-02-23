'''
3.6 复数的数学运算
问题
你写的最新的网络认证方案代码遇到了一个难题，并且你唯一的解决办法就是使
用复数空间。再或者是你仅仅需要使用复数来执行一些计算操作。
解决方案
复数可以用使用函数complex(real, imag) 或者是带有后缀j 的浮点数来指定。
'''
a = complex(2, 4)
print(a)

'''
对应的实部、虚部和共轭复数可以很容易的获取。
'''
print(a.real)
print(a.imag)
print(a.conjugate())

'''
讨论
Python 中大部分与数学相关的模块都能处理复数。比如如果你使用numpy ，可以
很容易的构造一个复数数组并在这个数组上执行各种操作
'''
import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(np.sin(a))

'''
Python 的标准数学函数确实情况下并不能产生复数值，因此你的代码中不可能会
出现复数返回值
如果你想生成一个复数返回结果，你必须显示的使用cmath 模块，或者在某个支
持复数的库中声明复数类型的使用
'''
import cmath
print(cmath.sqrt(-1))