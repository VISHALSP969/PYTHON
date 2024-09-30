# Getting unique elements of a list
restaurants=["McDonald's","Burger King","McDonald's","Chicken Chicken"]
unique_restaurants=set(restaurants)
print(unique_restaurants)

unique_restaurants=list(unique_restaurants)
print(unique_restaurants)

restaurants=["McDonald's","Burger King","McDonald's","Chicken Chicken","KFC"]
unique_restaurants=list(set(restaurants))
print(unique_restaurants)