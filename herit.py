# 多重继承
# MixIn
class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running')


class FlyableMixIn(object):
    def fly(self):
        print('Fly')


class CarnivorousMixIn(object):
    def run(self):
        print('Running')


class HerbivoresMixIn(object):
    def fly(self):
        print('Fly')


# 动物
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird):
    pass



# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类