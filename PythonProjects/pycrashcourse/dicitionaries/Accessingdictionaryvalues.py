# considering capitals as dictionary
capitals = {
    'Afghanisthan':'Kabul',
    'Algeria':'Aligers',
    'Argentina':'Buenos Aires',
    'Belgium':'Brussels',
    'Brasil':'Brazilia',
    'Bulgaria':'Sofia',
    'Canada':'OTTAWA',
    'Colombia':'Bogota',
    'CostaRica':'SanJose',
    'Denmark':'Copenhagen',
       
}

print(capitals)
# Adding a value to dictionary
print(capitals['Canada'])

capitals['UnitedKingdom'] = 'London'
print(capitals)

# removing the values or item from dictionary
del capitals['UnitedKingdom']
print(capitals)
# capitals = [
#     'Afghanisthan',
#     'Algeria',
#     'Argentina',
#     'Belgium',
#     'Brasil',
#     'Bulgaria',
#     'Canada',
#     'Colombia',
#     'CostaRica',
#     'Denmark'
       
# ]
# print(capitals[0])
# print(capitals[1])
# print(capitals[2])
# print(capitals[3])
# print(capitals[4])
# print(capitals[5])

# checking the existence of dictionary
print(capitals['Norway'])

print("Canada" in capitals)
print("UAE" in capitals)
# using the index
# If
if 'Argentina' in capitals:
    print(f"the capital of Argentina is {capitals['Argentina']}")