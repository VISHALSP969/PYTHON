class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('This is generic sound.')


class Dog(Animal):
    def sound(self):
        print(f'{self.name} barks.')


dog = Dog('Buddy')
dog.sound()
