# Types of Data types
# 1.Built In datattypes
# 2.User defined data types

# Numeric Data types
# 1.Int  : represents values or numbers without decimal values.Python there is no limit for int data type
num = 25
print(num)
print(type(num))

runs = 475896
print(runs)
print(type(runs))
# 2.Float 
# 1.Represents both  number and decimal values
# 2.Floating point numbers can be  written in scientific notation
# 3.e and E are exponentiation
# 4.e and E represent power of 10

b = 3650.98456
print(b)
print(type(b))

a = 3e6
print(a)
print(type(a))
c = 2E5
print(c)
print(type(c))
# 3.Complex 
# 1.represents the numbers written in form of a+bj or a-bj
# 2.a is the real part of number and
# 3.b is the imaginary part of number
a = 6+6j
print(a)
print(type(a))
b = 3-9j
print(type(b))
c = a+b
print(c)
print(type(c))
# comparison of two complex numbers leads to type error

# Boolean data types 
# 1.Bool data type represents boolean values in python
# 2.Bool Data type is only having two values those are
# a.True
# b.False
# 3.Represents True as 1 False as 0
# 4.Empty string represented as False
a = True
print(a)
print(type(a))  
b = False
print(b)
print(type(b))  
print(a+a)
print(a+b)

# None data type
# None datatype represents an object tht does not contain any value
# If object has no value  we can assign that object with none types
a = None
print(a)
print(type(a))