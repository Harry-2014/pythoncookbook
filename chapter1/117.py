'''
1.17 从字典中提取子集
问题
你想构造一个字典，它是另外一个字典的子集。
解决方案
最简单的方式是使用字典推导
'''
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
p1 = {key:value for key,value in prices.items() if value>200}
print(p1)
'''
讨论
大多数情况下字典推导能做到的，通过创建一个元组序列然后把它传给dict() 函
数也能实现。
'''
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)
'''
但是，字典推导方式表意更清晰，并且实际上也会运行的更快些（在这个例子中，
实际测试几乎比dcit() 函数方式快整整一倍）。
'''