'''
4.9 排列组合的迭代
问题
你想迭代遍历一个集合中元素的所有可能的排列或组合
解决方案
itertools 模块提供了三个函数来解决这类问题。其中一个是itertools.
permutations() ，它接受一个集合并产生一个元组序列，每个元组由集合中所有
元素的一个可能排列组成。也就是说通过打乱集合中元素排列顺序生成一个元组，
'''
items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)

'''
如果你想得到指定长度的所有排列，你可以传递一个可选的长度参数。
'''
for p in permutations(items, 2):
    print(p)

'''
使用itertools.combinations() 可得到输入集合中元素的所有的组合
'''
from itertools import combinations
for c in combinations(items, 3):
    print(c)

'''
对于combinations() 来讲，元素的顺序已经不重要了。也就是说，组合('a',
'b') 跟('b', 'a') 其实是一样的(最终只会输出其中一个)。
在计算组合的时候， 一旦元素被选取就会从候选中剔除掉(比如如果元
素’a’ 已经被选取了， 那么接下来就不会再考虑它了)。而函数itertools.
combinations_with_replacement() 允许同一个元素被选择多次，
'''