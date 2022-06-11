a =int(input("Enter no of rows"))
b = a
# outerloop
for c in range(a,0,-1):
    # innerloop
    for d in range(1, c+1):
        print(b, end="")
    print("")    