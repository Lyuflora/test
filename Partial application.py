# Partial application
# 偏函数

# ---默认参数---
import functools
def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s


power(5)
# ---------------


# functools.particial的作用是，把一个函数的某些参数固定住（设定默认值），返回一个新函数，这样调用更方便
int2 = functools.partial(int, base = 2)


print(int2('1000'))