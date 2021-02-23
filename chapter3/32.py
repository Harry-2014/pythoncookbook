'''
3.2 执行精确的浮点数运算
问题
你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现。
解决方案
浮点数的一个普遍问题是它们并不能精确的表示十进制数。并且，即使是最简单的
数学运算也会产生小的误差
如果你想更加精确(并能容忍一定的性能损耗)，你可以使用decimal 模块
Decimal对象会像普通浮点数一样的工作(支持所有的常用数学运算)。如果你打印它们或者在
字符串格式化函数中使用它们，看起来跟普通数字没什么两样。
decimal 模块的一个主要特征是允许你控制计算的每一方面，包括数字位数和四
舍五入运算。为了这样做，你先得创建一个本地上下文并更改它的设置
'''
from decimal import Decimal
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

'''
总的来说，decimal 模块主要用在涉及到金融的领域
当Python 和数据库打交道的时候也通常会遇到Decimal 对象，并且，通常也
是在处理金融数据的时候。
'''