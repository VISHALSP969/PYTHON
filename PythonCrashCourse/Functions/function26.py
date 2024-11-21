magicians=['Andrew','Michael','James','Thomas','John']

def show_magicians(names):
    for name in names:
        print(name)

def make_great(magicians):
    for i in range(0,len(magicians)):
        magicians[i]="Great "+magicians[i]
    return magicians

show_magicians(magicians)
new_magicians=make_great(magicians[:])
show_magicians(new_magicians)
show_magicians(magicians)