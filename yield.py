
def pow():
    for i in range(5):
        yield i
        
a = pow()   
b = iter(a)
print(next(b))


