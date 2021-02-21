'''
1.6 字典中的键映射多个值
问题
怎样实现一个键对应多个值的字典（也叫multidict）？
解决方案
一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你
就需要将这多个值放到另外的容器中，比如列表或者集合里面。
你可以很方便的使用collections 模块中的defaultdict 来构造这样的字典。
defaultdict 的一个特征是它会自动初始化每个key 刚开始对应的值，所以你只需要
关注添加元素操作了。
需要注意的是，defaultdict 会自动为将要访问的键（就算目前字典中并不存在
这样的键）创建映射实体。如果你并不需要这样的特性，你可以在一个普通的字典上使
用setdefault() 方法来代替
但是很多程序员觉得setdefault() 用起来有点别扭。因为每次调用都得创建一个
新的初始值的实例（例子程序中的空列表[] ）。
'''
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)