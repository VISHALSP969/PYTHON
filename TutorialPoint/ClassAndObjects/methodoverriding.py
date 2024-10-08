class Vehicle:
    def start(self):
        print('Starting the vehicle...')


class Car(Vehicle):
    def start(self):
        print('Starting the car...')

    def call_parent_method(self):
        super().start()


car = Car()
car.start()
car.call_parent_method()
