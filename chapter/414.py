'''
4.14 展开嵌套的序列
问题
你想将一个多层嵌套的序列展开成一个单层列表
解决方案
可以写一个包含yield from 语句的递归生成器来轻松解决这个问题。
'''
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)

'''
讨论
语句yield from 在你想在生成器中调用其他生成器作为子例程的时候非常有用。
如果你不使用它的话，那么就必须写额外的for 循环了。
最后要注意的一点是，yield from 在涉及到基于协程和生成器的并发编程中扮演
着更加重要的角色。
'''