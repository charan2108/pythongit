# title() is a method appears after the variable in the print statements
# A method is an action that a python performs  on a piece of data.The . after the name.title() tells
# the python to make the title() method act on the variable name
# every method  is followed by  a set of parenthesis
# methods often often needs  additional information to do their work 
name = 'ada lovelace'
print(name)
print(name.title())

# uppercase
name = 'ada lovelace'
print(name.upper())
# lowercase
name = 'ada lovelace'
print(name.lower())

# capitalize
name = 'ada lovelace'
print(name.capitalize())

# casefold
name = 'ada lovelace'
print(name.casefold())

#center
name = 'ada lovelace'
b= name.center(20)
print(b)
# count
name = 'ada lovelace'
c =  name.count('v')
print(c)

# encode
name = 'ada lovelace'
print(name.encode())