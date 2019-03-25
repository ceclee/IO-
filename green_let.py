from greenlet import greenlet

def test():
    print('111')
    b.switch()
    print('222')
    b.switch()

def test2():
    print('333')
    a.switch()
    print('444')

a = greenlet(test)
b = greenlet(test2)
print(a)
print(type(a))
a.switch()