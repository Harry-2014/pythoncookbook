'''
2.1 使用多个界定符分割字符串
问题
你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格) 并不是固定
的。
解决方案
string 对象的split() 方法只适应于非常简单的字符串分割情形，它并不允许有
多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候，
最好使用re.split() 方法
'''
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
aa = re.split(r'[;,\s]\s*', line)
print(aa)
'''
讨论
函数re.split() 是非常实用的，因为它允许你为分隔符指定多个正则模式。比如，
在上面的例子中，分隔符可以是逗号，分号或者是空格，并且后面紧跟着任意个的空
格。只要这个模式被找到，那么匹配的分隔符两边的实体都会被当成是结果中的元素返
回。返回结果为一个字段列表，这个跟str.split() 返回值类型是一样的。
当你使用re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括
号捕获分组。如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中。
获取分割字符在某些情况下也是有用的。
'''
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(''.join(v+d for v,d in zip(values, delimiters)))
