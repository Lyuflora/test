def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

calc_sum(1,2)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


def outer( a ):
    b = 10
    # inner是内函数
    def inner():
        c = 2
        #在内函数中 用到了外函数的临时变量
        print(a+b+c)
        # 外函数的返回值是内函数的引用
    return inner
demo = outer(5)
demo()

demo2 = outer(4)
demo2()