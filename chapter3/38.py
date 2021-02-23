'''
3.8 分数运算
问题
你进入时间机器，突然发现你正在做小学家庭作业，并涉及到分数计算问题。或者
你可能需要写代码去计算在你的木工工厂中的测量值。
解决方案
fractions 模块可以被用来执行包含分数的数学运算。
'''
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
c = a * b
print(c.numerator)
print(c.denominator)
