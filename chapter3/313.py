'''
3.13 计算最后一个周五的日期
问题
你需要查找星期中某一天最后出现的日期，比如星期五。
解决方案
Python 的datetime 模块中有工具函数和类可以帮助你执行这样的计算
'''
from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
'Friday', 'Saturday', 'Sunday']
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

datetime.today()
print(get_previous_byday('Monday'))
print(get_previous_byday('Sunday', datetime(2012, 12, 21)))