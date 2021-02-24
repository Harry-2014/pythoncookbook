'''
3.15 字符串转换为日期
问题
你的应用程序接受字符串格式的输入，但是你想将它们转换为datetime 对象以便
在上面执行非字符串操作。
解决方案
使用Python 的标准模块datetime 可以很容易的解决这个问题。
'''
from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

'''
讨论
datetime.strptime() 方法支持很多的格式化代码，比如%Y 代表4 位数年份，%m
代表两位数月份。还有一点值得注意的是这些格式化占位符也可以反过来使用，将日期
输出为指定的格式字符串形式
还有一点需要注意的是，strptime() 的性能要比你想象中的差很多，因为它是使
用纯Python 实现，并且必须处理所有的系统本地设置。如果你要在代码中需要解析大
量的日期并且已经知道了日期字符串的确切格式，可以自己实现一套解析方案来获取
更好的性能。比如，如果你已经知道所以日期格式是YYYY-MM-DD ，你可以像下面这样
实现一个解析函数
'''
from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
