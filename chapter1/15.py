'''
1.5 实现一个优先级队列
问题
怎样实现一个按优先级排序的队列？并且在这个队列上面每次pop 操作总是返回
优先级最高的那个元素
解决方案
下面的类利用heapq 模块实现了一个简单的优先级队列：

'''

import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
'''
这一小节我们主要关注heapq 模块的使用。函数heapq.heappush() 和heapq.
heappop() 分别在队列_queue 上插入和删除第一个元素，并且队列_queue 保证第一
个元素拥有最高优先级（1.4 节已经讨论过这个问题）。heappop() 函数总是返回”最小
的”的元素，这就是保证队列pop 操作返回正确元素的关键。另外，由于push 和pop
操作时间复杂度为O(log N)，其中N 是堆的大小，因此就算是N 很大的时候它们运行
速度也依旧很快。
在上面代码中，队列包含了一个(-priority, index, item) 的元组。优先级为负
数的目的是使得元素按照优先级从高到低排序。这个跟普通的按优先级从低到高排序
的堆排序恰巧相反。
index 变量的作用是保证同等优先级元素的正确排序。通过保存一个不断增加的
index 下标变量，可以确保元素按照它们插入的顺序排序。而且，index 变量也在相同
优先级元素比较的时候起到重要作用。
如果你使用元组(priority, item) ，只要两个元素的优先级不同就能比较。但是
如果两个元素优先级一样的话，那么比较操作就会跟之前一样出错：
通过引入另外的index 变量组成三元组(priority, index, item) ，就能很好的
避免上面的错误，因为不可能有两个元素有相同的index 值。Python 在做元组比较时
候，如果前面的比较已经可以确定结果了，后面的比较操作就不会发生了
'''
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())