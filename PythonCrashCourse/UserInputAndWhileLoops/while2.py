prompt="\nPlease enter the name of a city you have visites : "
prompt+="\n(Enter 'quit' when you are finished.)\n"

while True:
    city=input(prompt)

    if city=='quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")