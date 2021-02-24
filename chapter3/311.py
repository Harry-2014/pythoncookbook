'''
3.11 随机选择
问题
你想从一个序列中随机抽取若干元素，或者想生成几个随机数。
解决方案
random 模块有大量的函数用来产生随机数和随机选择元素。比如，要想从一个序
列中随机的抽取一个元素，可以使用random.choice()
'''
import random

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.choice(values))

#为了提取出N 个不同元素的样本用来做进一步的操作，可以使用random.sample()
print(random.sample(values, 2))

#如果你仅仅只是想打乱序列中元素的顺序，可以使用random.shuffle()
'''
random()是Python的随机数函数，shuffle()方法可以将输入的列表数据->打乱顺序->重新输出。

但是如果直接打印print，就会返回None，没有显示正确数据。

所以不能打印shuffle()方法，只能打印值
'''
random.shuffle(values)
print(values)

#生成随机整数，请使用random.randint()
print(random.randint(0,10))

#为了生成0 到1 范围内均匀分布的浮点数，使用random.random()
print(random.random())

#如果要获取N 位随机位(二进制) 的整数，使用random.getrandbits()
print(random.getrandbits(200))

'''
讨论
random 模块使用Mersenne Twister 算法来计算生成随机数。这是一个确定性算
法，但是你可以通过random.seed() 函数修改初始化种子。
'''
random.seed()
print(random.seed(12345))

