# 装饰器 fuctional decorators
# 本质上，decorator是一个返回函数的高阶函数


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 如上，log接收一个函数作为参数，并返回一个函数
# 借助@语法：
@log
def now():
    print('2015-3-25')

# 如上，相当于调用了now = log(now)


now()
# Output:call now():
#   call now():
#   2015-3-25


# 如果decorator本身需要参数，
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2019-3-31')


now()


# 一个完整的decorator
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper