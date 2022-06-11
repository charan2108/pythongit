# Modifying elements in a list

bikes=['honda', 'suzuki', 'ducati']
print(bikes)
# modifying
bikes[0]='Tomcat'
print(bikes)
print("="*40)
# Adding Elements to lis
# append
bikes=['honda', 'suzuki', 'ducati']
print(bikes)
bikes.append('Tomcat')

print("="*40)
# appending elements tp end of the list
bikes.append('Ninja')
print(bikes)

print("="*40)
# empty list
motobikes= []
motobikes.append('Honda')
motobikes.append('Hellcat')
motobikes.append('Ducati')
motobikes.append('Suzuki')
print(motobikes)

print("="*40)
# Removing elements from list
# del method
bikes=['honda', 'suzuki', 'ducati']
print(bikes)
del(bikes[0])
print(bikes)
print("="*40)

# pop method
bikes=['honda', 'suzuki', 'ducati']
print(bikes)
bikes.pop(0)
print(bikes)

bikes=['honda', 'suzuki', 'ducati']
print(bikes)

popped_bikes= bikes.pop()
print(popped_bikes)
# poping from position in a list
popped_bikes= bikes.pop(1)
print(popped_bikes)

# removing item
bikes=['honda', 'suzuki', 'ducati']
print(bikes)
bikes.remove('honda')
print(bikes)