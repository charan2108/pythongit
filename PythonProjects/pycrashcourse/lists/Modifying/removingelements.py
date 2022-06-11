bikes = ['ducati', 'honda', 'extreme', 'cbz','pulsar']
# del the bikes
del bikes[4]
print(bikes)

# popmethod
popped_bikes= bikes.pop()
print(popped_bikes)

last_owned_bike = bikes.pop()
print("My last owned bike: " + last_owned_bike.title()+"!")

# remove method
bikes.remove('ducati')
print(bikes)