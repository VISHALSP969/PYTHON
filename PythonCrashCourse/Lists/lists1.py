bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# accessing elements in a list
print(bicycles[0])  # first item index - 0
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
# negative index also possible
print(bicycles[-1])  # last item index - -1
print(bicycles[-2])  # second last item
print(bicycles[-3])
print(bicycles[-4])

print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
