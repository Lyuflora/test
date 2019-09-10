#匿名函数
list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9]))


#lambda x :x*x 实际上就是：
def f(x):
    return x*x
#可以把匿名函数赋值给一个变量，再利用变量调用该函数
f = lambda x: x*x
f
print(f)
#也可把匿名函数作为返回值返回
def build(x,y):
    return lambda: x*x+y*y

def is_odd(n):
    return n%2==1


lambda x: x%2==1
L = list(filter(lambda x: x%2==1, range(1,20)))