class Restaurant:
    def __init__(self,name,cuisine_type):
        self.name=name.title()
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        msg=f"{self.name} serves wonderful {self.cuisine_type}"
        print(f"\n{msg}")

    def open_restaurant(self):
        msg=f"{self.name} is open. come on in!"
        print(f"\n{msg}")

    def set_number_served(self,number_served):
        self.number_served=number_served

    def increment_number_served(self,additional_served):
        self.number_served+=additional_served