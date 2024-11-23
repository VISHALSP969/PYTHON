def order_sandwich(*sandwichs):
    print("Orders")
    for sandwich in sandwichs:
        print("-"+sandwich)

order_sandwich('Veg Sandwich','Chicken Sandwich','Italian Sandwich')