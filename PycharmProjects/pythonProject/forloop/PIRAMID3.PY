a =int(input("Enter number of rows"))
b = 0
for c in range(a,0,-1):
    b+=1
    for d in range(1, c+1):
        print(b, end=" ")
    print('\r')

a =int(input("Enter number of rows"))
b = 0
for c in range(a,0,-1):
    b+=1
    for d in range(1, c+1):
        print(d, end=" ")
    print('\r')