# Polymorphism
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('A dog is running...')
    
    def eat(self):
        print('A dog is eating...')


class Cat(Animal):
    pass


dog = Dog()
dog.run()
cat = Cat()
cat.run()
print(dir(dog))
