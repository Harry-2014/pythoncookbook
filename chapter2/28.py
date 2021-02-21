'''
2.8 多行匹配模式
问题
你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。
解决方案
这个问题很典型的出现在当你用点(.) 去匹配任意字符的时候，忘记了点(.) 不能
匹配换行符的事实。比如，假设你想试着去匹配C 语言分割的注释：
'''
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multiline comment */'''
print(comment.findall(text1))
print(comment.findall(text2))
'''
为了修正这个问题，你可以修改模式字符串，增加对换行的支持

'''
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

'''
讨论
re.compile() 函数接受一个标志参数叫re.DOTALL ，在这里非常有用。它可以让
正则表达式中的点(.) 匹配包括换行符在内的任意字符。
'''
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
