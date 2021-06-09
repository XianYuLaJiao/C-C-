"""
标准库 time
处理时间相关的方法
"""
import time

# 三种类方法 ：时间戳 结构化时间对象 格式化时间字符串

# 1.时间戳 1970.1.1 到指定时间的间隔，单位是秒
print(time.time())

# 2.结构化时间对象
st = time.localtime()
print(type(st))  # <class 'time.struct_time'>
print(st)  # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=1, tm_hour=16, tm_min=55, tm_sec=32, tm_wday=6,
# tm_yday=306, tm_isdst=0)
# st本质上是一个元组，一共9个元素time.struct_time(tm_year=2020, tm_mon=11, tm_mday=1, tm_hour=16, tm_min=42, tm_sec=52, tm_wday=6,
# tm_yday=306, tm_isdst=0),对象的属性是只读的不能修改的
print('今天是{}-{}-{}'.format(st[0], st[1], st[2]))
print('今天是星期{}'.format(st.tm_wday + 1))

# 3.格式化的时间字符串
print(time.ctime())  # Sun Nov  1 16:55:32 2020
# strftime(参数：时间格式)’%Y-%M-%D %H:%M:%S‘
print(time.strftime('%Y年-%m月-%d日 %H:%M:%S %p')) # 占位符为%加一个字母，大小写的含义不同，%Y表示数字年，%m表示数字月份，%d表示数字天。%H表示数字小时（24进制）

# %M表示数字分钟，%S表示数字秒，%p表示pm或者pa,%a，%A表示英文星期的简全写，%b,%B表示英文月份简全写，其他的- ：月 都不是占位符，是普通的字符串。

# sleep
t1 = time.time()
print("sleep begin...")
time.sleep(5)# 参数是int单位为秒
print('sleep end')
t2 =time.time()
print('执行了{:.3f}秒'.format(t2-t1))