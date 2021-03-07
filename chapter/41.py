'''
4.1 手动遍历迭代器
问题
你想遍历一个可迭代对象中的所有元素，但是却不想使用for 循环。
解决方案
为了手动的遍历可迭代对象，使用next() 函数并在代码中捕获StopIteration 异
常
'''
def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

'''
通常来讲，StopIteration 用来指示迭代的结尾。然而，如果你手动使用上面演示
的next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如None 。
'''
items = [1, 2, 3]
it = iter(items) # Invokes items.__iter__()
print(next(it))
print(next(it))