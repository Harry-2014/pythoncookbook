'''
1.14 排序不支持原生比较的对象
问题
你想排序类型相同的对象，但是他们不支持原生的比较操作。
解决方案
内置的sorted() 函数有一个关键字参数key ，可以传入一个callable 对象给
它，这个callable 对象对每个传入的对象返回一个值，这个值会被sorted 用来排序
这些对象。比如，如果你在应用程序里面有一个User 实例序列，并且你希望通过他们
的user_id 属性进行排序，你可以提供一个以User 实例作为输入并输出对应user_id
值的callable 对象。
attrgetter('user_id')
'''
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
# def sort_notcompare():
users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))
'''
讨论
选择使用lambda 函数或者是attrgetter() 可能取决于个人喜好。但是，
attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较。这
个跟operator.itemgetter() 函数作用于字典类型很类似
同样需要注意的是，这一小节用到的技术同样适用于像min() 和max() 之类的函
数。
min(users, key=attrgetter('user_id'))
max(users, key=attrgetter('user_id'))
'''
by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
