'''
1.19 转换并同时计算数据
问题
你需要在数据序列上执行聚集函数（比如sum() , min() , max() ），但是首先你需
要先转换或者过滤数据
解决方案
一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数。
'''
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Determine if any .py files exist in a directory
# import os
# files = os.listdir('dirname')
'''
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
元素除了是 0、空、FALSE 外都算 TRUE。
'''
# if any(name.endswith('.py') for name in files):
#     print('There be python!')
# else:
#     print('Sorry, no python.')
# Output a tuple as CSV
s = ('ACME', 50, 123.45)
# join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
print(','.join(str(x) for x in s))
# Data reduction across fields of a data structure
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)