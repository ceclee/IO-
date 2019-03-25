
#测试用！！


def recursion(i):   #定义函数
    print(i)
    if i/2 > 1:   #判断递归条件，退出
        re = recursion(i/2)  #递归函数自身
        print('返回值:',re)
    print('上层递归值：',i)
    return i     #返回值

recursion(10)