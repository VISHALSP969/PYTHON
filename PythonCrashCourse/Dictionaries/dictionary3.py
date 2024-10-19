alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# modifying values in dictionary
alien_0['color'] = 'yellow'
print(alien_0)

alien_1={'x-position':0,'y-position':25,'speed':'medium'}
print('Original x-position : '+str(alien_1['x-position']))

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_1['speed']=='slow':
    x_increment=1
elif alien_1['speed']=='medium':
    x_increment=2
else:
    # this must be a fast alien
    x_increment=3

# the new position is the old position plus the increment
alien_1['x-position']=alien_1['x-position']+x_increment

print('New x-position : '+str(alien_1['x-position']))