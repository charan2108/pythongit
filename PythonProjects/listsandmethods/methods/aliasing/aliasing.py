# process of giving a new name to existing name is known as aliasing
a = [10,20,30]
b = a
print(a)
print(b)
print(id(a))
print(id(b))

a[2] = 50
print(a)
print(b)
print(id(a))
print(id(b))
