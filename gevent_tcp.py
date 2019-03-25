import gevent
from gevent import monkey
monkey.patch_all() #monkey脚本插件导入要在socket之前，他改变了socket模块的阻塞部分
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('localhost',8888))
s.listen(20)

def handler(c,addr):
    rec = c.recv(1024).decode()
    print(rec)
    print('recv from:',addr)
    c.send(b'good!'+rec.encode())
    c.close()

while True:
    c,addr = s.accept()
    gevent.spawn(handler,c,addr)

s.close()
