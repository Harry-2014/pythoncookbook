'''
3.16 结合时区的日期操作
问题
你有一个安排在2012 年12 月21 日早上9:30 的电话会议，地点在芝加哥。而你
的朋友在印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？
解决方案
对几乎所有涉及到时区的问题，你都应该使用pytz 模块。这个包提供了Olson 时
区数据库，它是时区信息的事实上的标准，在很多语言和操作系统里面都可以找到。
pytz 模块一个主要用途是将datetime 库创建的简单日期对象本地化。
建议使用UTC模块
'''
from datetime import datetime
from pytz import timezone
d = datetime(2012, 12, 21, 9, 30, 0)
print(d)
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

