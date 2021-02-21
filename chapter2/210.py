'''
2.10 在正则式中使用Unicode
问题
你正在使用正则表达式处理文本，但是关注的是Unicode 字符处理。
解决方案
默认情况下re 模块已经对一些Unicode 字符类有了基本的支持。比如，\\d 已经
匹配任意的unicode 数字字符了：
'''

import re
num = re.compile('\d+')
print(num.match('123'))
print(num.match('\u0661\u0662\u0663'))

'''
讨论
混合使用Unicode 和正则表达式通常会让你抓狂。如果你真的打算这样做的话，最
好考虑下安装第三方正则式库，它们会为Unicode 的大小写转换和其他大量有趣特性
提供全面的支持，包括模糊匹配。
'''
