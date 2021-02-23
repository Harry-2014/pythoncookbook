'''
3.3 数字的格式化输出
问题
你需要将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节。
解决方案
格式化输出单个数字的时候，可以使用内置的format() 函数
'''
x = 1234.56789
print(format(x, '0.2f'))

# Right justified in 10 chars, one-digit accuracy
print(format(x, '>10.1f'))

# Left justified
print(format(x, '<10.1f'))

# Centered
print(format(x, '^10.1f'))

# Inclusion of thousands separator
print(format(x, ','))

print(format(x, '0,.1f'))

'''如果你想使用指数记法，将f 改成e 或者E(取决于指数输出的大小写形式)。'''
print(format(x, 'e'))
print(format(x, '0.2E'))