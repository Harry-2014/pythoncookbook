'''
4.10 序列上索引值迭代
问题
你想在迭代一个序列的同时跟踪正在被处理的元素索引。
解决方案
内置的enumerate() 函数可以很好的解决这个问题
'''
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

'''
为了按传统行号输出(行号从1 开始)，你可以传递一个开始参数
'''
for idx, val in enumerate(my_list, 1):
    print(idx, val)

'''
讨论
当你想额外定义一个计数变量的时候，使用enumerate() 函数会更加简单
enumerate() 函数返回的是一个enumerate 对象实例，它是一个迭代器，返回连
续的包含一个计数和一个值的元组，元组中的值通过在传入序列上调用next() 返回。
还有一点可能并不很重要，但是也值得注意，有时候当你在一个已经解压后的元组
序列上使用enumerate() 函数时很容易调入陷阱
data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
# Correct!
for n, (x, y) in enumerate(data):

# Error!
for n, x, y in enumerate(data):
'''
