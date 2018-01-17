# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多进程

# Windows下的多进程 -> multiprocessing 模块，创建一个子进程
from multiprocessing import Process
import os
# 子进程代码
def child_process(name):
    print('Name %s || Parant %s || Child %s' % (name, os.getppid(), os.getpid()))

# 当直接执行文件时调用
if __name__ == '__main__':
    print('Parent %s' % os.getpid())
    p = Process(target=child_process, args=('test', ))
    p.start() # 启动
    p.join() # 等待子进程结束后继续运行，用于进程间的同步



# 启动大量子进程可使用进程池Pool
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Task %s(%s) start' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s end after %0.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent %s' % os.getpid())
    p = Pool(4) # 设为4个时，若跑5了个进程，则前4个按顺序运行，第5个暂时挂起，当其中一个进程结束时，让第5个任务加入运行，详细可见输出结果
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waitting')
    p.close() # 不再添加新进程
    p.join() # 等待所有子进程完成
    print('All done')



# 创建一个子进程并控制其输入输出 -> subprocess 模块
import subprocess
# 输出
print('cmd: nslookup www.baidu.com')
r = subprocess.call(['nslookup', 'www.baidu.com'])
print('exit code:', r)
# 输入
print('cmd: nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n') # 等于向命令行输入了nslookup加上这里的bytes数据
print(output.decode('GBK')) # 转换bytes为GBK(PS: 使用utf-8会报错)
print('Exit code:', p.returncode)



# 进程间通信 -> multiprocessing
# Queue -> 在父进程中创建两个子进程，一写一读
from multiprocessing import Process, Queue
import os, time, random
# 写
def write(q):
    print('Process to write %s' % os.getpid()) 
    for v in ['A', 'B', 'C']:
        print('Put %s in queue...' % v)
        q.put(v)
        time.sleep(random.random())
# 读
def read(q):
    print('Process to read %s' % os.getpid())
    while True:
        v = q.get(True)
        print('Get %s from queue' % v)

if __name__ == '__main__':
    # 父进程创建Queue并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()
    # 等待pw结束
    pw.join()
    # 由于pr是死循环，需要手动结束
    pr.terminate()