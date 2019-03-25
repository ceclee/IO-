import gevent,time

def foo1():
    print('a')
    gevent.sleep(2)
    print(3)

def foo2():
    print(2)
    gevent.sleep(2)
    print(4)

a = gevent.spawn(foo1)
b = gevent.spawn(foo2)

gevent.joinall([a,b])
