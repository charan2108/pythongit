# Syntax
# string.capitalize()
a = 'welcome to coding'
print(a)
b = a.capitalize()
print(b)

# casefold
# synatax
# string.casefold()
c = "Hello, welcome to the session on Python"
print(c)
d = c.casefold()
print(d)

# center
# syntax
# string.center(length, character)
e = "Grapes"
print(e)
f = e.center(30)
print(f)
f = e.center(50, '-')
print(f)

# count
# syntax
# string.count(value,start,end)

g = 'apple are apple'
print(g)
h = g.count('apple')
print(h)

para = '''
 This method of combining strings is called concatenation. You can use
concatenation to compose complete messages using the information you’ve
stored in a variable
'''
r=para.count('o')
print(r)

# encode
# syntax
# string.encode(encoding=encoding, errors=errors)
name="My name is stash"
print(name)
s = name.encode()
print(s)

# string ends
# syntax
# string.endswith(value, start,end)
msg = "Hello welcome to python crash course."
print(msg)
c=msg.endswith('.')
print(c)
msg = "Hello welcome to python crash course."
print(msg)
c=msg.endswith('course.')
print(c)
msg = "Hello welcome to python crash course."
print(msg)
c=msg.endswith('course.', 5, 11)
print(c)

# expand tabs
# string.expandtabs(tabsize)
a = 'P\ty\tt\th\to\tn'
print(a)
r = a.expandtabs(2)
print(r)
r = a.expandtabs(4)
print(r)
r = a.expandtabs(6)
print(r)
r = a.expandtabs(8)
print(r)
r = a.expandtabs(10)
print(r)

# find method
# syntax
# string.find(vlaue, start, end)
mode = 'This is, python coding'
y = mode.find('coding')
print(y)

mode = 'This is, Ansys World'
y = mode.find('A')
print(y)

# Format method
# string.format(value1,value2)
txt="For only {price: .2f} $!"
print(txt.format(price = 49))
txt="For only {price: .2f} dollars!"
print(txt.format(price = 49))
# placeholders
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age =36)
print(txt1)

# Index Method
# string.index(value,start,end)
skid = "Hello, Welcome to the coding language."
s = skid.index('coding')
print(s)
skid = "Hello, Welcome to the coding language."
s = skid.index('c')
print(s)

# isalnum
# syntax
# string.isalnum()
card ="Webstercard33"
d = card.isalnum()
print(d)

# isalpha
# Syntax
# string.isalpha()
ser = "completecompanyX"
s = ser.isalpha()
print(s)

# isascii
# syntax
# string.ascii()
ascii = "Company33"
q = ascii.isascii()
print(q)

# isdecimal
# syntax
# string.isdecimal()
code_transfer = "\u0033"
f = code_transfer.isdecimal()
print(f)

# isdigit
# syntax
# string.isdigit()
g = '50500'
h = g.isdigit()
print(h)

# isidentifier
# syntax
# string.isidentifier()
Hello = "Python"
p = Hello.isidentifier()
print(p)

# islower
# syntax
# string.islower()
name="Adam Lovelace"
w = name.islower()
print(w)

# isnumeric
# syntax
# string.isnumeric()
air = '54567'
i = air.isnumeric()
print(i)

# isprintable()
# syntax
# string.isprintable()

r = "Hello are you #1"
er = r.isprintable()
print(er)

# isplace
# syntax
# string.isplace()
y = "  "
d = y.isspace()
print()

# istitle()
# syntax
# string.istitle()
Name = 'adam lovelace'
a = Name.istitle()
print(a)
# isupper()
# syntax
# string.isupper()
Name = 'adam lovelace'
a = Name.isupper()
print(a)

# Join
# syntax
# string.join()
name = ('John', 'sander','lee')
c = "-".join(name)
# c = "#".join(name)
# c = ",".join(name)
# c = ".".join(name)
# c = "/".join(name)
# c = "'".join(name)
print(c)
# dictionary
myDict = {"name": "Jack", "country":"United States"}
a ="Hello"
d = a.join(myDict)
print(d)

# ljustify
a ='Grapes'
b =a.ljust(20)
print(b,"is a fruit")
a ='Grapes'
b =a.ljust(20, "O")
print(b,"is a fruit")

