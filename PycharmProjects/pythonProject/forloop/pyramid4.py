a = int(input("Enter no of rows"))
for b in range(a, 0, -1):
    for c in range(0, b+1):
        print(c, end=' ')
    print('\r')

a = int(input("Enter no of rows"))
for b in range(a, 0, -1):
    for c in range(0, b+1):
        print(b, end=' ')
    print('\r')