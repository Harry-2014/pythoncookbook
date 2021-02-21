'''
1.12 序列中出现次数最多的元素
问题
怎样找出一个序列中出现次数最多的元素呢？
解决方案
collections.Counter 类就是专门为这类问题而设计的，它甚至有一个有用的
most_common() 方法直接给了你答案。
'''
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
print(word_counts)
# 出现频率最高的3 个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

'''
讨论
作为输入，Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列
对象。在底层实现上，一个Counter 对象就是一个字典，将元素映射到它出现的次数
上。
'''
morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print(word_counts)
'''
Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。
'''
a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)
d = a - b
print(d)