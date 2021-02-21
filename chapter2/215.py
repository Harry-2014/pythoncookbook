'''
2.15 字符串中插入变量
问题
你想创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。
解决方案
Python 并没有对在字符串中简单替换变量值提供直接的支持。但是通过使用字符
串的format() 方法来解决这个问题。
'''
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

'''
如果要被替换的变量能在变量域中找到，那么你可以结合使用format_map()
和vars()
'''
name = 'Guido'
n = 37
print(s.format_map(vars()))

'''
vars() 还有一个有意思的特性就是它也适用于对象实例
'''
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('Guido',37)
print(s.format_map(vars(a)))

'''
format 和format_map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况
一种避免这种错误的方法是另外定义一个含有__missing__() 方法的字典对象

'''
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

print(s.format_map(safesub(vars())))

import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))

'''
format() 和format_map() 相比较上面这些方案而已更加先进，因此应该
被优先选择。使用format() 方法还有一个好处就是你可以获得对字符串格式化的所有
支持(对齐，填充，数字格式化等待)，而这些特性是使用像模板字符串之类的方案不可
能获得的。
本机还部分介绍了一些高级特性。映射或者字典类中鲜为人知的__missing__()
方法可以让你定义如何处理缺失的值。在SafeSub 类中，这个方法被定义为对缺失的
值返回一个占位符。你可以发现缺失的值会出现在结果字符串中(在调试的时候可能很
有用)，而不是产生一个KeyError 异常。
sub() 函数使用sys._getframe(1) 返回调用者的栈帧。可以从中访问属性
f_locals 来获得局部变量。毫无疑问绝大部分情况下在代码中去直接操作栈帧应
该是不推荐的。但是，对于像字符串替换工具函数而言它是非常有用的。另外，值得注
意的是f_locals 是一个复制调用函数的本地变量的字典。尽管你可以改变f_locals
的内容，但是这个修改对于后面的变量访问没有任何影响。所以，虽说访问一个栈帧看
上去很邪恶，但是对它的任何操作不会覆盖和改变调用者本地变量的值
'''