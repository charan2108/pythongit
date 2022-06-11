a = int(input("Enter the no of rows"))
# outerloop
for b in range(1,a):
    # innerloop
    for c in range(b,0,-1):
        print(c,end="")
    print("")     