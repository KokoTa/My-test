# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多线程(和多进程多核利用不同，多线程是单核交替运行)

# 启动线程 -> threading
import time, threading

def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('Tread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Tread %s end' % threading.current_thread().name)


print('Thread %s is running...' % threading.current_thread().name) # 主线程
t = threading.Thread(target=loop, name='LoopThread') # 支线程
t.start()
t.join()
print('Tread %s end' % threading.current_thread().name)



# 多线程情况下修改同一全局变量会导致执行顺序错乱，从而导致结果错误
# 为了保证执行结果正确要给线程加锁，保证不造成修改冲突 -> treading.Lock()
balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run(n):
    for i in range(100000):
        # 要先获取锁，使这个线程单独执行，而不是两个线程一起进行
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 完了要解锁
            lock.release()

t1 = threading.Thread(target=run, args=(5,))
t2 = threading.Thread(target=run, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



# 线程中，局部数据在函数中的传递 -> treading.local()
# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# 创建全局ThreadLocal对象
local_school = threading.local()

def process_thread(name):
    # 绑定在ThreadLocal
    local_school.student = name
    process_student()

def process_student():
    # 获取ThreadLocal上的student
    std = local_school.student
    print('Name %s in %s' % (std, threading.current_thread().name))

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()