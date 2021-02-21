'''
2.12 审查清理文本字符串
问题
一些无聊的幼稚黑客在你的网站页面表单中输入文本”pýtĥöñ”，然后你想将这些
字符清理掉。
解决方案
文本清理问题会涉及到包括文本解析与数据处理等一系列问题。在非常简单的情
形下，你可能会选择使用字符串函数(比如str.upper() 和str.lower() ) 将文本转为
标准格式。使用str.replace() 或者re.sub() 的简单替换操作能删除或者改变指定
的字符序列。你同样还可以使用2.9 小节的unicodedata.normalize() 函数将unicode
文本标准化。
然后，有时候你可能还想在清理操作上更进一步。比如，你可能想消除整个区间上
的字符或者去除变音符。为了这样做，你可以使用经常会被忽视的str.translate()
方法
'''
s = 'pýtĥöñ\fis\tawesome\r\n'
'''
第一步是清理空白字符。为了这样做， 先创建一个小的转换表格然后使用
translate() 方法
'''
remap = {
ord('\t') : ' ',
ord('\f') : ' ',
ord('\r') : None # Deleted
}
a = s.translate(remap)

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

'''
讨论
文本字符清理一个最主要的问题应该是运行的性能。一般来讲，代码越简单运行越
快。对于简单的替换操作，str.replace() 方法通常是最快的，甚至在你需要多次调用
的时候。
'''
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s
'''
如果你去测试的话，你就会发现这种方式会比使用translate() 或者正则表达式
要快很多。
另一方面，如果你需要执行任何复杂字符对字符的重新映射或者删除操作的话，
tanslate() 方法会非常的快。
'''