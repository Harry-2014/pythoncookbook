'''
2.3 用Shell 通配符匹配字符串
问题
你想使用Unix Shell 中常用的通配符(比如*.py , Dat[0-9]*.csv 等) 去匹配文
本字符串
解决方案
fnmatch 模块提供了两个函数——fnmatch() 和fnmatchcase() ，可以用来实现
这样的匹配。

'''
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
'''
fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的) 来
匹配模式
如果你对这个区别很在意，可以使用fnmatchcase() 来代替。它完全使用你的模
式大小写匹配。
'''
print(fnmatchcase('foo.txt', '*.TXT'))
'''
这两个函数通常会被忽略的一个特性是在处理非文件名的字符串时候它们也是很
有用的。
'''
addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
from fnmatch import fnmatchcase
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])

'''
讨论
fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。如果在
数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案。
'''
