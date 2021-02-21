'''
1.16 过滤序列元素
问题
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
解决方案
最简单的过滤序列元素的方法就是使用列表推导
'''
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n>0])
print([n for n in mylist if n<0])

'''
使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结
果集，占用大量内存。如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生
过滤的元素
'''
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

'''
有时候，过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中表达出
来。比如，假设过滤的时候需要处理一些异常或者其他复杂情况。这时候你可以将过滤
代码放到一个函数中，然后使用内建的filter() 函数。
'''
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except:
        return False

iValues = list(filter(is_int,values))
print(iValues)

'''
讨论
列表推导和生成器表达式通常情况下是过滤数据最简单的方式。
过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们。比
如，在一列数据中你可能不仅想找到正数，而且还想将不是正数的数替换成指定的数。
通过将过滤条件放到条件表达式中去，可以很容易的解决这个问题

'''
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
'''
另外一个值得关注的过滤工具就是itertools.compress() ，它以一个iterable
对象和一个相对应的Boolean 选择器序列作为输入参数。然后输出iterable 对象中对
应选择器为True 的元素。当你需要用另外一个相关联的序列来过滤某个序列的时候，
这个函数是非常有用的。
'''
addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK',
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
# 将大于5的值全部输出
more5 = [n > 5 for n in counts]
print(more5)
lst = list(compress(addresses, more5))
print(lst)
'''
这里的关键点在于先创建一个Boolean 序列，指示哪些元素符合条件。然后
compress() 函数根据这个序列去选择输出对应位置为True 的元素。
和filter() 函数类似，compress() 也是返回的一个迭代器。因此，如果你需要得
到一个列表，那么你需要使用list() 来将结果转换为列表类型。
'''