sandwich_orders = ['steak sandwich', 'pastrami sandwich', 'falafel sandwich', 'pastrami sandwich', 'buffet sandwich',
                   'club sandwich', 'pastrami sandwich', 'ribbon sandwich', 'pinwheel sandwich', 'grilled sandwich']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("Made all sandwiches")

if sandwich_orders.count('pastrami sandwich'):
    print("Delivery has run out of pastrami")

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
print(sandwich_orders)

for sandwich in sandwich_orders:
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("Made all sandwiches")

poll_record = {}
poll_active = True

while poll_active:
    name = input("What is your name?\n")
    place = input("Where do you want go on vacation?\n")

    poll_record[name] = place

    choice = input("Do you want to add another response? (yes/no)\n")
    if choice == 'no':
        poll_active = False

print(poll_record)
for name, place in poll_record.items():
    print(name + " want to go to " + place + " on vacation")
