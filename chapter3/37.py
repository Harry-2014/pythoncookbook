'''
3.7 无穷大与NaN
问题
你想创建或测试正无穷、负无穷或NaN(非数字) 的浮点数。
解决方案
Python 并没有特殊的语法来表示这些特殊的浮点值，但是可以使用float() 来创
建它们。
'''
import math
a = float('inf')
b = float('-inf')
c = float('nan')
'''
为了测试这些值的存在，使用math.isinf() 和math.isnan() 函数。
'''
print(math.isinf(a))
print(math.isnan(c))

'''
无穷大数在执行数学计算的时候会传播
但是有些操作时未定义的并会返回一个NaN 结果
NaN 值会在所有操作中传播，而不会产生异常
NaN 值的一个特别的地方时它们之间的比较操作总是返回False。
由于这个原因，测试一个NaN 值得唯一安全的方法就是使用math.isnan() 
'''

