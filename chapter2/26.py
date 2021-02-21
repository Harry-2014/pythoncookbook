'''
2.6 字符串忽略大小写的搜索替换
问题
你需要以忽略大小写的方式搜索与替换文本字符串
解决方案
为了在文本操作时忽略大小写，你需要在使用re 模块的时候给这些操作提供
re.IGNORECASE 标志参数。
'''
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))

print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

'''
讨论
对于一般的忽略大小写的匹配操作，简单的传递一个re.IGNORECASE 标志参数就
已经足够了
'''