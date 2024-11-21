magicians=['Andrew','Michael','James','Thomas','John']

def show_magicians(names):
    for name in names:
        print(name)

def make_great():
    for i in range(0,len(magicians)):
        magicians[i]='Great '+magicians[i]

show_magicians(magicians)
make_great()
show_magicians(magicians)