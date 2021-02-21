'''
2.2 字符串开头或结尾匹配
问题
你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL
Scheme 等等。
解决方案
检查字符串开头或结尾的一个简单方法是使用str.startswith() 或者是str.
endswith() 方法
如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
给startswith() 或者endswith() 方法：
'''
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

'''
奇怪的是，这个方法中必须要输入一个元组作为参数。如果你恰巧有一个list 或
者set 类型的选择项，要确保传递参数前先调用tuple() 将其转换为元组类型。
'''
'''
讨论
startswith() 和endswith() 方法提供了一个非常方便的方式去做字符串开头和
结尾的检查。类似的操作也可以使用切片来实现，但是代码看起来没有那么优雅。
'''
