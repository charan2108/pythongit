guests = ['Alfa', 'Beta', 'charlie', 'delta']
print(guests)
print("You have been invited to"+guests[0].title()+"!")
print("You have been invited to"+guests[1].title()+"!")
print("You have been invited to"+guests[2].title()+"!")
print("You have been invited to"+guests[3].title()+"!")

# Changing the guests lists
guests.insert(1, 'echo')
print("You have been invited to"+guests[0].title()+"!")
print("You have been invited to"+guests[1].title()+"!")
print("You have been invited to"+guests[2].title()+"!")
print("You have been invited to"+guests[3].title()+"!")
print(guests)

guests.insert(4, 'foxtrot')
guests.insert(5, 'Hotel')
print("You have been invited to"+guests[0].title()+"!")
print("You have been invited to"+guests[1].title()+"!")
print("You have been invited to"+guests[2].title()+"!")
print("You have been invited to"+guests[3].title()+"!")
print("You have been invited to"+guests[4].title()+"!")
print("You have been invited to"+guests[5].title()+"!")
print(guests)


guests = ['Alfa', 'Beta', 'charlie', 'delta']
guests.append('India')
guests.append('Juliet')
guests.append('Kilo')
guests.append('Lima')
print(guests)