a =int(input("Enter number of rows"))
for b in range(1,6):
    c = 65
    for d in range(1, b+1):
        print(chr(c), end="")
        c+=1
    print("")

a =int(input("Enter number of rows"))
for b in range(1,6):
    c = 65
    for d in range(1, b-1):
        print(chr(d), end="")
        c+=1
    print("")
