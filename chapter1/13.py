'''
1.3 保留最后N 个元素
    问题:
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
    解决方案:
保留有限历史记录正是collections.deque 大显身手的时候
我们在写查询元素的代码时，通常会使用包含yield 表达式的生成器函数，也就
是我们上面示例代码中的那样
使用deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并
且这个队列已满的时候，最老的元素会自动被移除掉。
尽管你也可以手动在一个列表上实现这一的操作（比如增加、删除等等）。但是这
里的队列方案会更加优雅并且运行得更快些。
'''


from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        lst = search(f, 'python', 3)
        for line, prevlines in lst:
            for pline in prevlines:
                print(pline, end='')
                print(line, end='')
                print('-' * 20)
    fab(5)