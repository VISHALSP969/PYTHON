def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print("- "+topping)

make_pizza('Pepperoni')
make_pizza('Mushrooms','Green peppers','Extra cheese')