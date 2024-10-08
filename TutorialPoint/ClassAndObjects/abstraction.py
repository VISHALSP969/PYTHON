from abc import ABC, abstractmethod


# Abstract class
class Vehicle(ABC):
    # Abstract method
    @abstractmethod
    def start_engine(self):
        pass

    # Abstract method
    @abstractmethod
    def stop_engine(self):
        pass


# Concrete class - Car
class Car(Vehicle):
    def start_engine(self):
        print('Car engine started')

    def stop_engine(self):
        print('Car engine stopped')


# Concrete class - Bike
class Bike(Vehicle):
    def start_engine(self):
        print('Bike engine started')

    def stop_engine(self):
        print('Bike engine stopped')


# Create objects of Car and Bike
my_car=Car()
my_bike=Bike()

# Demonstrating abstraction by calling the start_engine and stop_engine methods
print('Car operations')
my_car.start_engine()
my_car.stop_engine()

print('Bike operations')
my_bike.start_engine()
my_bike.stop_engine()
