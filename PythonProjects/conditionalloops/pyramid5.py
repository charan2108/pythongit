a = int(input('enter no of rows'))
# outerloop
for b in range(a,0,-1):
    # innerloop
    for c in range(0, b+1):
        print(c, end="")
    print('\r')    
        