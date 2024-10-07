class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display_info(self):
        print(f'Car model : {self.model} , Color : {self.color}')


# Creating an object of the car class
my_car = Car('Toyota', 'White')
my_car.display_info()
