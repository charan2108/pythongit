# Range Function
for a in range(1,11):
    print(a)

for a in range(1,21):
    print(a)

for a in range(1,15):
    print(a)
    

    #using numbers to make the range function easier
num = list(range(1,50))
print(num)

#Even numbers 
e_num = list(range(2,20,2))
print(e_num)

# Odd Numbers
o_num = list(range(1,20,2))
print(o_num)

# square
squares = []
for a in range(1,13):
    b = a**2
    squares.append(b)
print(squares)

squares = [a**2 for a in range(1,13)]
print(squares)

# cubes
cubes = []
for a in range(1,13):
    b = a**3
    cubes.append(b)
print(cubes) 

cubes = [a**3 for a in range(1,13)] 
print(cubes)  
# statistics
num = [1,2,3,4,5,6,7,8,9,10]
print(num)
print(min(num))
print(max(num))