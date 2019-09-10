# 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
# Python内置的@property装饰器就是负责把一个方法变成属性调用
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self._score = value

s = Student()
s.score = 60
print(s.score)


class Screen(object):


    @property
    def width(self):
        return self._width


    @width.setter
    def width(self, value):
        self._width = value


    @property
    def height(self, value):
        return self._height


    @height.setter
    def height(self, value):
        self._height = value


    @property
    def resolution(self):
        return self._height*self._width


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')