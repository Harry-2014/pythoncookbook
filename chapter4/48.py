'''4.8 跳过可迭代对象的开始部分
问题
你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。
解决方案
itertools 模块中有一些函数可以完成这个任务。首先介绍的是itertools.
dropwhile() 函数。使用时，你给它传递一个函数对象和一个可迭代对象。它会返
回一个迭代器对象，丢弃原有序列中直到函数返回Flase 之前的所有元素，然后返回后
面所有元素'''

# User Database
##
#Note that this file is consulted directly only when the system is running
# in single-user mode. At other times, this information is provided by
# Open Directory.
...
##
'''nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh'''

from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

'''
这个例子是基于根据某个测试函数跳过开始的元素。如果你已经明确知道了要跳
过的元素的个数的话，那么可以使用itertools.islice() 来代替。
'''
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)