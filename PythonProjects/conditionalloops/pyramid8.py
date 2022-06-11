a = int(input("Enter number of rows"))
# outerloop
for c in range(1, a):
    b = 1
    # innerloop
    for d in range(a,0,-1):
        if d > c:
            print(" ", end="")
        else:
            print(b, end="")
            b += 1
    print("")            
                