# 类和对象
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score 

    def print_score(self):
        print('%s, %s' % (self.name, self.__score))

    def get_score(self):
        return self.__score

    def set_score(self, mark):
        self.__score = mark


# "__"开头的变量是私有的 private
bart = Student('Bart', 99)
print(bart)
bart.print_score()
bart.name


# 前后双下划线的是特殊变量，是可以直接访问的
