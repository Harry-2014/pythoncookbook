'''
问题
你想通过某种对齐方式来格式化字符串
解决方案
对于基本的字符串对齐操作，可以使用字符串的ljust() , rjust() 和center()
方法。
'''
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.rjust(20,'='))

'''
函数format() 同样可以用来很容易的对齐字符串。你要做的就是使用<,> 或者^
字符后面紧跟一个指定的宽度
'''
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

'''
当格式化多个值的时候，这些格式代码也可以被用在format() 方法中
'''
print('{:>10s} {:>10s}'.format('Hello', 'World'))
'''
format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值，使
得它非常的通用。
'''
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))

'''
在新版本代码中，你应该优先选择format() 函数或者方法。format() 要比
% 操作符的功能更为强大。并且format() 也比使用ljust() , rjust() 或center() 方
法更通用，因为它可以用来格式化任意对象，而不仅仅是字符串。
'''