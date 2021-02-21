'''
1.8 字典的运算
问题
怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
解决方案
为了对字典值执行计算操作，通常需要使用zip() 函数先将键和值反转过来。
执行这些计算的时候，需要注意的是zip() 函数创建的是一个只能访问一次的迭
代器。
如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是
值
前面的zip() 函数方案通过将字典”反转”为(值，键) 元组序列来解决了上述问
题。当比较两个元组的时候，值会先进行比较，然后才是键。这样的话你就能通过一条
简单的语句就能很轻松的实现在字典上的求最值和排序操作了。
需要注意的是在计算操作中使用到了(值，键) 对。当多个实体拥有相同的值的时
候，键会决定返回结果。
'''
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
# max_price is (612.78, 'AAPL')
'''
类似的，可以使用zip() 和sorted() 函数来排列字典数据：
'''
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
# (45.23, 'ACME'), (205.55, 'IBM'),
# (612.78, 'AAPL')]
