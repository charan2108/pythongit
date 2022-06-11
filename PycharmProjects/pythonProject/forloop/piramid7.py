a = int(input("Enter the number of rows"))
for b in range(0, a+1):
    for c in range(a-b,0,-1):
        print(c, end="")
    print("")
