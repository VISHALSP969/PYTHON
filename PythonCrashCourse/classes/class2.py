class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name.title()
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        msg=f"{self.restaurant_name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg=f"{self.restaurant_name} is open,come on in!"
        print(f"\n{msg}")

restaurant=Restaurant('the mean queen','pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
