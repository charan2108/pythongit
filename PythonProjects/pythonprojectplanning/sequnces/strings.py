# Sequences in python are objects that can store group of values
# the squences are 
# 1.String
# 2.Bytes
# 3.bytearray
# 4.list
# 5.tuple
# 6.Range

# Strings
# 1.A group of characters enclosed within a single quotes or double quotes or triple quotes is called string
# Single quotation
name = 'Welcome World'
print(name)
print("=" * 40)
# double quotations
print("=" * 40)
name = "Welcome World"
print(name)
print("=" * 40)
# triple quotations
name = '''Welcome World'''
print(name)
print("=" * 40)
# Camelcase Method
print("=" * 40)
name = "ada lovelace"
print("Before camel case method :",name)
print("After camelcase method :",name.title())
print("=" * 40)
# Capitalize method converts first character of a string to uppercase letter and lowercases 
# string.capitalize()
# Capitalize method
name_1 = "will smith"
print(name_1.capitalize())
print("=" * 40)
# Casefold() method  is an aggressive lower method converts strings to case folded strings for caseless matching
# Casefold() method removes all case distinctions present in a string
msg = "WELCOME TO PYTHON"
print(msg)
print(msg.casefold())
print("=" * 40)
# center method returns the string padded with specified character
# string.center(width[, fillchar])
# width - length of string with padded character
# optional with  padding characters
print("=" * 40)
msg = "Welcome to coding"
print(msg)
print(msg.center(25))
print("=" * 40)

# fillchar method
msg = "Welcome to coding"
print(msg)
print(msg.center(25, '/'))
print("=" * 40)
# Upperlowercase method
name = "ada lovelace"
print(name.lower())
print(name.upper())
print("=" * 40)
# Count method
# string.count(substring, start=,end=)
code = "Alfa Romeo"
print(name)
print(name.count('o'))
print(name.count('a'))
print("=" * 40)
print(code)
print(code.count('o'))
print(code.count('a'))
print("=" * 40)
# countsbustring
substring='Romeo'
a = code.count(substring)
print(a)
print("=" * 40)
# encode
# string.encode(encoding='',errors='strict')
c = 'Coding language'
print(c.encode())
# EndsWith
# str.endswith(suffix[, start[, end]])
coding = 'Coding is always a fun thing'
print(coding)
print(coding.endswith('fun thing'))
# expandtabs
# string.expand(tabsize)
a = '123\t welcome\t 456'
print(a)
b = a.expandtabs()
print(b)
print("=" * 40)
# expandtab with different arguement
c = 'abc\t 123 \t coding'
d = c.expandtabs(5)
e = c.expandtabs(7)
print(d)
print(e)
print("=" * 40)
# find method
# str.find(sub[, start[, end]] )
languages = 'python is the simplest yet a complex programming'
print(languages)
print(languages.find('complex'))
print("=" * 40)
# format method 
#  template.format(p0,p1,)
# default arguments
print("Hello {}, your balance is {}".format('Chari', 336.590))
# positional arguments
print("Hello {0}, your balance is {1}".format('Chari', 336.590))
# keyword arguments
print("Hello {name}, your balance is {bal}".format(name='Chari', bal=336.590))
# mixed
print("Hello {0}, your balance is {bal}".format('Chari', bal=336.590))
print("=" * 40)
# format_map
a = {'n': 4 , 'o': 5}
print('{n} {o}'.format_map(a))
a = {'n': 4 , 'o': 5 , 'p' : -9}
print('{n} {o} {p}'.format_map(a))
print("=" * 40)

# StringIndex
text = 'coding is fun'
b = text.index('fun')
print(b)
print("=" * 40)

# isalpha
name = "codingMguys123"
print(name.isalnum())
print(name.isalpha())
# isdecimal
s = '33669988'
print(s.isdecimal())