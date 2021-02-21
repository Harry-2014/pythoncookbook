'''
2.16 以指定列宽格式化字符串
问题
你有一些长字符串，想以指定的列宽将它们重新格式化。
解决方案
使用textwrap 模块来格式化字符串的输出
'''
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent=' '))
print(textwrap.fill(s, 40, subsequent_indent=' '))

'''
讨论
textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端
大小的时候。你可以使用os.get_terminal_size() 方法来获取终端的大小尺寸。

'''
import os
print(os.get_terminal_size().columns)

'''
fill() 方法接受一些其他可选参数来控制tab， 语句结尾等
'''