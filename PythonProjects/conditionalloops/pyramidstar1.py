# a = int(input("Enter no of rows"))
# for b in range(1, a+1):
#     for c in range(1,b+1):
#         print("*", end="")
#     print("")    
 
# a = int(input("Enter no of rows"))
# for b in range(a+1, 0,-1):
#     for c in range(1,b+1):
#         print("*", end="")
#     print("")  

a = int(input("Enter no of rows"))
d = 1
for b in range(1, a+1):
    for c in range(1,d+1):
        print("*", end="")
        d+=2
    print("")   