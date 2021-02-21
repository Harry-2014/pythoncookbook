'''
2.14 合并拼接字符串
问题
你想将几个小的字符串合并为一个大的字符串
解决方案
如果你想要合并的字符串是在一个序列或者iterable 中，那么最快的方式就是使
用join() 方法。
'''
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

'''
初看起来，这种语法看上去会比较怪，但是join() 被指定为字符串的一个方法。
这样做的部分原因是你想去连接的对象可能来自各种不同的数据序列(比如列表，元
组，字典，文件，集合或生成器等)，如果在所有这些对象上都定义一个join() 方法明
显是冗余的。因此你只需要指定你想要的分割字符串并调用他的join() 方法去将文本
片段组合起来。
如果你仅仅只是合并少数几个字符串，使用加号(+) 通常已经足够了
'''
'''
讨论
最重要的需要引起注意的是，当我们使用加号(+) 操作符去连接大量的字符串的
时候是非常低效率的，因为加号连接会引起内存复制以及垃圾回收操作。
'''
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ''.join(sample())
print(text)

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)
# 结合文件操作
with open('filename', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)
