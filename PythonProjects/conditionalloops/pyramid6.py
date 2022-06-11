a =int(input("Enter no of rows"))
# outerloop
for c in range(a,0,-1):
    b = c
    for d in range(0,c):
        print(b, end="")
    print('\r')       