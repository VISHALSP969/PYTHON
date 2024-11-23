def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza(16,"Pepperoni")
make_pizza(12,"Mushrooms","Green peppers","Extra cheese")
