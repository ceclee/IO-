from socket import *
import select,sys

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('localhost',8889))
s.listen(5)

rlist = [s]
wlist = []
xlist = [s]

while True:
    #监听三个关注的列表中的io事件
    rs,ws,es = select.select(rlist,wlist,xlist)
    print('等了一个世纪~~~~~~,come')
    #通过for循环遍历每个返回列表，去处理IO
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print('connect from',addr)
            # c.send(b'uuuuuuuu')
            rlist.append(c)
            xlist.append(c)
        else:
            wlist.append(r)
            data = r.recv(1024).decode()
            if not data:
                print('客户端退出')
                rlist.remove(r)
                xlist.remove(r)
                r.close()

            print('shoudao',data) 
            r.send(b'good!')

    for w in ws:
        w.send(b'aaaaaaaaaaaa')
        wlist.remove(w)

    for e in es:
        if e is s:
            s.close()
            sys.exit(0)
        else:
            rlist.remove(e)
            xlist.remove(e)
            e.close()


        
s.close()
