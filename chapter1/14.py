'''
1.4 查找最大或最小的N 个元素
问题
怎样从一个集合中获得最大或者最小的N 个元素列表？
解决方案
heapq 模块有两个函数：nlargest() 和nsmallest() 可以完美解决这个问题。\
两个函数都能接受一个关键字参数，用于更复杂的数据结构中：
如果你想在一个集合中查找最小或最大的N 个元素，并且N 小于集合元素数量，
那么这些函数提供了很好的性能。
堆数据结构最重要的特征是heap[0] 永远是最小的元素。并且剩余的元素可以很
容易的通过调用heapq.heappop() 方法得到，该方法会先将第一个元素弹出来，然后
用下一个最小的元素来取代被弹出元素（这种操作时间复杂度仅仅是O(log N)，N 是
堆大小）
当要查找的元素个数相对比较小的时候，函数nlargest() 和nsmallest() 是很
合适的。如果你仅仅想查找唯一的最小或最大（N=1）的元素的话，那么使用min() 和
max() 函数会更快些。类似的，如果N 的大小和集合大小接近的时候，通常先排序这个
集合然后再使用切片操作会更快点（sorted(items)[:N] 或者是sorted(items)[-N:]
）。需要在正确场合使用函数nlargest() 和nsmallest() 才能发挥它们的优势（如果
N 快接近集合大小了，那么使用排序操作会更好些）。
'''

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)