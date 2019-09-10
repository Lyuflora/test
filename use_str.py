class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__


print(Student('Micheal'))


# 一个类被用于for循环
class Fib(object):
    # init, iter, next
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    # 像list一样能取某个下标的值  
    def __getitem__(self, n):
        if isinstance(n, int):  # 如果n是下标，根据索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):  # 如果n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L


for n in Fib():
    print(n)


f = Fib()
print(f[4])  # 输出：5

print(f[: 10])
# 暂时还没有完成step和负参数的分类讨论

# 此外，如果把对象看成dict，
# #__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，
# 用于删除某个元素。


# 调用不存在的属性时，解释器会调用getattr
class Son(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Son\' object has no attribute \'%s\'' % attr)
    