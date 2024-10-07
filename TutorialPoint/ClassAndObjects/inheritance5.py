class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")


# Child class that inherits from Animal
class Cat(Animal):
    def __init__(self, name, breed):
        # Calling parent class constructor
        super().__init__(name)
        self.breed = breed

    def sound(self):
        # Calling parent class sound method
        super().sound()
        print(f'{self.name} meows.')


# Creating an instance of the Cat class
cat = Cat('Whiskers', 'Siamese')
cat.sound()
