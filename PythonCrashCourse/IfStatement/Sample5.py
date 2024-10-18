requested_toppings = ['mushroom', 'onions', 'pineapple']
print('mushroom' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
