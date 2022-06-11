# a ="Hello"
# print(a)
# print(len(a))
# print(type(a))
# print(id(a))
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# mystery =734_529.678
# print(mystery)
# print(type(mystery))
# a = len(input("Enter the two digit"))
# b = str(a) 
# print("Upur name has"+ b +"characters")

# a =123
# print(type(a))

# a =str(123)
# print(type(a))
# two_digit_number = input("Type a two digit number: ")
# a = two_digit_number[0]
# b = two_digit_number[1]
# c = int(a) +int(b)
# print(c)

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 20

c = a & b;        # 12 = 0000 1100
print( "Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c
)
c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)