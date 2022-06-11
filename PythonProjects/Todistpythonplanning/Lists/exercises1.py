# Make a list that  at least contains three people to invite for a party
guest_list = ['Alfa','Beta','Charlie']
print(guest_list)

print("You are invited to "+guest_list[0].title() +" Party at lord's")
print("You are invited to "+guest_list[1].title() +"Party at lord's")
print("You are invited to "+guest_list[2].title() +"Party at lord's")

# changing the guests list 
# At the moment ine of your guest is not attending print out new cards
guest_list = ['Alfa','Beta','Charlie']
print(guest_list)

guest_list.remove('Charlie')
print(guest_list)
# add the new guests
guest_list.append('deltas')
print(guest_list)
print("You are invited to "+guest_list[0].title() +" Party at lord's")
print("You are invited to "+guest_list[1].title() +" Party at lord's")
print("You are invited to "+guest_list[2].title() +" Party at lord's")
# Expand the guest lists by using the methods u have learnt

guest_list = ['Alfa','Beta','Charlie']
print(guest_list)

guest_list.insert(0, 'Echo')
print(guest_list)
guest_list.insert(2, 'Foxtrot')
print(guest_list)
guest_list.append('Hotel')
print(guest_list)


