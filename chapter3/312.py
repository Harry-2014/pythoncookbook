'''
3.12 基本的日期与时间转换
问题
你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换。
解决方案
为了执行不同时间单位的转换和计算，请使用datetime 模块。比如，为了表示一
个时间段，可以创建一个timedelta 实例
'''
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4)
c = a + b
print(c)
print(c.days)
print(c.seconds)

'''
如果你想表示指定的日期和时间，先创建一个datetime 实例然后使用标准的数学
运算来操作它们。
在计算的时候，需要注意的是datetime 会自动处理闰年。
'''
from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))

now = datetime.today()
print(now + timedelta(minutes=10))

'''
讨论
对大多数基本的日期和时间处理问题，datetime 模块已经足够了。如果你需要执
行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等，可以考虑使
用dateutil 模块
许多类似的时间计算可以使用dateutil.relativedelta() 函数代替。但是，有一
点需要注意的就是，它会在处理月份(还有它们的天数差距) 的时候填充间隙
'''