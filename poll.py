import select
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('localhost',8888))
s.listen(5)

#以每个io对象的fileno为键，io对象为值
fdmap = {s.fileno():s}

#创建poll对象
p = select.poll()

#添加关注的io
p.register(s)

while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('connect from',addr)
            #将客户端套接字添加关注并添加到字典
            p.register(c)
            fdmap[c.fileno()] = c
        else:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)
                fdmap[fd].send(b'shoudao!')



