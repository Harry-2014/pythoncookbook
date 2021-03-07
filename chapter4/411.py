'''
4.11 同时迭代多个序列
问题
你想同时迭代多个序列，每次分别从一个序列中取一个元素。
解决方案
为了同时迭代多个序列，使用zip() 函数。
'''
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62,99]
for x, y in zip(xpts, ypts):
    print(x,y)

'''
zip(a, b) 会生成一个可返回元组(x, y) 的迭代器，其中x 来自a，y 来自b。一
旦其中某个序列到底结尾，迭代宣告结束。因此迭代长度跟参数中最短序列长度一致。
如果这个不是你想要的效果，那么还可以使用itertools.zip_longest() 函数来
代替。
'''
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)

'''
讨论
当你想成对处理数据的时候zip() 函数是很有用的
使用zip() 可以让你将它们打包并生成一个字典

'''
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers,values))
'''
最后强调一点就是，zip() 会创建一个迭代器来作为结果返回。如果你需要将结对
的值存储在列表中，要使用list() 函数
list(zip(a, b))
'''
