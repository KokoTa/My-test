# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# TCP编程

# 客户端
# 建立一个socket等于建立了一个网络连接
# 创建一个socket并连接服务器
import socket
# AF-INET IPv4协议; AF-INET6 IPv6协议； SOCK_STREAM 面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接，连接服务器的80端口（80端口是Web服务的标准端口）
# SMTP服务是25端口，FTP服务是21端口
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()
# 切分数据
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)


# 服务端
# 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
import socket, threading, time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
# listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024) # 得到bytes数据
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 通过一个永久循环来接受来自客户端的连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    # 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
    # 这里就当作一个用户对应一个客服
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()





# UDP编程

# 服务端
import socket
# SOCK_DGRAM UDP协议
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
# 不需要listen()方法
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024) # 返回数据和地址
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
# 省掉了多线程