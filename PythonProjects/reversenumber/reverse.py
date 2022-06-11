a = int(input("Enter the number"))
b = 0

while a>0:
    c = a % 10
    b = (b * 10) + c
    a = a//10
print("{}".format(b))    

    