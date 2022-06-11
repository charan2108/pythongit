
alien_0 = {'color':'green', 'points':25}

print(alien_0)

alien_0['color'] = 'red'

print(alien_0)


alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}

print("Orginal position is "+str(alien_0['x_position']))

if alien_0 =='slow':
    x_increment = 1
elif alien_0 == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("nw position is "+str(alien_0['x_position']))       