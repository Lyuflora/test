# 给实例绑定方法
class Student(object):
    pass


s = Student()
s.name = 'Micheal'
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)

print(s.age)


# 给class绑定方法  动态绑定允许我们再成都程序运行的过程中动态给class加上功能
def set_score(self, score):
    self.score = score


Student.set_score = set_score


# 想要限制实例的属性
# Python允许在定义class的时候，定义一个特殊的__slots__变量
class Student(object):
    __slots__ = ('name',  'age') # 用tuple定义允许绑定的属性名称


s = Student()
s.name = 'Micheal' # z在slot中出现
s.age = 25 # z在slot中出现
s.score = 99
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。