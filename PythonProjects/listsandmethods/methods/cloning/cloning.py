# The process of creating independent duplicate objects is called cloning
# Can be implemented by using slicing operator or by using copy command
# the process of creating a duplicate object of the existing one is allocated to different memory
# objects r independent
# will not impact each other
a = ['a', 'b', 'c', 'd']
b = a[:]
print(a)
print(b)
print(id(a))
print(id(b))
a[3] = 'f'
print(a)
print(b)
print(id(a))
print(id(b))