'''
1.13 通过某个关键字排序一个字典列表
问题
你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
解决方案
通过使用operator 模块的itemgetter 函数，可以非常容易的排序这样的数据结
构。
'''
rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
'''
itemgetter() 函数也支持多个keys，比如下面的代码
'''
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

'''
讨论
在上面例子中，rows 被传递给接受一个关键字参数的sorted() 内置函数。这个
参数是callable 类型，并且从rows 中接受一个单一元素，然后返回被用来排序的值。
itemgetter() 函数就是负责创建这个callable 对象的。
operator.itemgetter() 函数有一个被rows 中的记录用来查找值的索引参数。可
以是一个字典键名称，一个整形值或者任何能够传入一个对象的__getitem__() 方法
的值。如果你传入多个索引参数给itemgetter() ，它生成的callable 对象会返回一
个包含所有元素值的元组，并且sorted() 函数会根据这个元组中元素顺序去排序。
itemgetter() 有时候也可以用lambda 表达式代替，比如：
'''
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
'''
这种方案也不错。但是，使用itemgetter() 方式会运行的稍微快点。因此，如果
你对性能要求比较高的话就使用itemgetter() 方式。
min(rows, key=itemgetter('uid'))
max(rows, key=itemgetter('uid'))
'''