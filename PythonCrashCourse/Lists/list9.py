# Indentation error
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician.title() + ",that was a great trick!")      # indentation error
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")
# print("Thank you, everyone. That was a great magic show!")

# forgetting to indent additional lines
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

print("\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

print("\n")

# Indenting unnecessarily
# message="Hello Python world!"
#     print(message)        # unexpexted indent

# Indenting unnecessarily after the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you, everyone. That was a great magic show!")

print("\n")

# forgetting th colon
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians           # syntax error
#     print(magician.title() + ",that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")
# print("Thank you, everyone. That was a great magic show!")

