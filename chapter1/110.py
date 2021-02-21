'''
1.10 删除序列相同元素并保持顺序
问题
怎样在一个序列上面保持元素顺序的同时消除重复的值？
解决方案
如果序列上的值都是hashable 类型，那么可以很简单的利用集合或者生成器来解
决这个问题。
这个方法仅仅在序列中元素为hashable 的时候才管用。
'''
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
aa = list(dedupe(a))
print(aa)

'''
如果你想消除元素不可哈
希（比如dict 类型）的序列中重复元素的话，你需要将上述代码稍微改变一下
'''
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
aa = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print(aa)
aa = list(dedupe(a, key=lambda d: d['x']))
print(aa)
'''
讨论
如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合
set(a)
然而，这种方法不能维护元素的顺序，生成的结果中的元素位置被打乱。而上面的
方法可以避免这种情况。
上述key 函数参数模仿了sorted() , min() 和max() 等内置函数的相似功能。
'''