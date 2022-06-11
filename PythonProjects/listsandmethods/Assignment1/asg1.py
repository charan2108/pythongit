# defining list
L = ['michael Jackson', 10.1, 1982]
# printing a list
print(L)
# indexing list
print(L[0])
print(L[1])
print(L[2])
# indexing negative indexing
print(L[0])
print(L[1])
print(L[2])

# list content
# L = ['michael Jackson', 10.1, 1982, [1, 2], ("A", 10)]
# print(L)
# print(type(L))
# In case of printing last two letters
L = ['michael Jackson', 10.1, 1982, "MJ", 1]
print(L[3:5])
# extend
L.extend(['thriller', 100])
L.extend(['a', 'b'])
print(L)
# append
L.append(['1million copies', 10000])
L.append(['a', 'b'])
print(L)
# mutability
A = ['disco', 10, 1.2]
print("before changing list a", A)
A[0] = 'Pop'
print("list after changing A", A)

# del
A = ['disco', 10, 1.2]
del(A[0])
print(A)

# Spliting
a = 'Sports Network'
print(a)
b = a.split()
print(b)
d = 's.p.o.r.t.s'.split('.')
print(d) 
# copy/clone
A = ['disco', 10, 1.2]
B = A
print("A:", A)
print("B:", B)

A = ['disco', 10, 1.2]
print("B[0]:", B[0] )
A[0] = "Banna"
print("B[0]:", B[0] )

B=A[:]
print(B)

