# use the loop for printing 1 to 20
for a in range(1,21):
    print(a)
#make a list of numbers from one to one milion print it 
# min and max in the million
# odd numbers
odd_numbers = list(range(1,11,2))
print(odd_numbers)
# list of multiples 3 to 30
for m in range(3,37,3):
    print(m)
# cubes
cubes = []
for a in range(1,11):
    cube = a**3
    cubes.append(cube)
print(cubes)    
# comprehension
cubes=[a**3 for a in range(1,11)]
print(cubes)