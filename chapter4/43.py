'''
4.3 使用生成器创建新的迭代模式
问题
你想实现一个自定义迭代模式，跟普通的内置函数比如range() , reversed() 不
一样。
解决方案
如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。下面是一个生产
某个范围内浮点数的生成器：
'''
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)

'''
讨论
一个函数中需要有一个yield 语句即可将其转换为一个生成器。跟普通函数不同
的是，生成器只能用于迭代操作
'''
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))

'''
一个生成器函数主要特征是它只会回应在迭代中使用到的next 操作。一旦生成器
函数返回退出，迭代终止。我们在迭代中通常使用的for 语句会自动处理这些细节，所
以你无需担心。
'''