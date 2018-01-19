# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python常用模块 - datetime 模块

# 获取当前时间
from datetime import datetime
print('获取当前时间:')
now = datetime.now()
print(now)
print(type(now))

# 获取指定时间
print('获取指定时间:')
dt = datetime(2015, 4, 19, 12, 20) 
print(dt)

# 获取时间戳
print('获取时间戳:')
ts = dt.timestamp()
print(ts)

# 时间戳转本地标准时间 -> UTC+8:00
print('时间戳转本地标准时间:')
dt = datetime.fromtimestamp(ts)
print(dt)

# 时间戳转格林威治时间 -> UTC+0:00
print('时间戳转格林威治时间:')
dt = datetime.utcfromtimestamp(ts)
print(dt)

# str转时间，转换后没有时区信息
print('str转时间:')
dt = datetime.strptime('2015-1-1 12:12:12', '%Y-%m-%d %H:%M:%S')
print(dt)

# 时间转str
print('时间转str:')
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# 时间加减 -> timedelta
print('时间加减:')
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=1, hours=12))

# 时间转UTC时间,其实就是加个时区信息
print('时间转UTC时间:')
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
now = now.replace(tzinfo=tz_utc_8) # tzinfo 时区属性
print(now)

# 时区转换
# 拿到utc时间并强制设置时区为UTC+0:00
print('时区转换:')
utc_dt = datetime.utcnow()
print(utc_dt)
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()强制转换为其他时区
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# 练习：给定时间和日期，以及一个时区，将其转换为时间戳
import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
  tz_hour = re.match(r'UTC([+|-]\d+):00', tz_str).group(1) # 正则似乎需要完全匹配，不然会出错
  tz = timezone(timedelta(hours=int(tz_hour)))
  return datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz).timestamp()
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t2)
