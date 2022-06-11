a =int(input("Enter no of rows"))
b = 0
# outerloop
for c in range(a, 0, -1):
    b+= 1
    for d in range(1, c+1):
        print(b, end="")
    print(" ")    
        
