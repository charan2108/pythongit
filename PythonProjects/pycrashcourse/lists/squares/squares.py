squares = []

for a in range(1,13):
    b = a**2
    squares.append(b)
print(squares)    

# oneliner
squares = [a**2 for a in range(1,13)]
print(squares)

cubes = []

for c in range(1,13):
    d = c**3
    cubes.append(d)
print(cubes) 

cubes=[c**3 for c in range(1,13)]
print(cubes)   