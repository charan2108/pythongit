# print("Hello World!")
# a = 1
# b = 2
# x = a + b
# x = 10

# print(X)

# the intensity = 125.11
# print(the intensity)

# x=str(float(int('2')))
# print(x)

# if not 1 in [10, 20] and 1 < 2:
#     print(1)
# else:
#     print(2)

# a= list(range(2, 5)) 
# print(a)

# animals = ['bear', 'rat', 'cow', 'shrimp', 'shark']
# print(animals[2:])
# numbers = ('a', 'b', 1, 2)
# print(numbers[3])

# air_temperature = [35, 28, 10]
# land_temperature = [18, 20, 15]
# x =air_temperature[1] + land_temperature[0]
# print(x)

# mylist = [['abc'], ['def', 'ghi']]
# print(mylist[-1][-1][-1])

# d = {
#     "food": {
#         "rice":
#             {
#                 "weight": 30.1,
#                 "taste": "good",
#                 "forms": ["boiled"]
#             },
#         "banana":
#             {
#                 "weight": 19,
#                 "taste": "excellent",
#             }
#         }
# }
 
# print(d['food']['banana']['taste'])

# def eur_to_usd(euros, rate=0.8):
#     return euros * rate
# print(eur_to_usd(10))

# x = 10.0
 
# if type(x) == float:
#     print(int(x))
# else:
#     print(x)

# x = 10
# y = 11
 
# if x > 10 and y > 10:
#     print("Success!")
# else:
#     print("Failed!")
# items = ['adapter', 'cable', 'keyboard']
 
# choice = input("Item")
# if choice in items:
#     print("Item is available!")
# weight = float(input("How many kg?"))
# price = weight * 2.5
# print(f"Price is [price]")

# weight = float(input("How many kg?"))
# price = weight * 2.5
# print(f"Price is {price}")

# weight = float(input("How many kg?"))
# price = weight * 2.5
# print(f"Price is {price}")

for letter in 'abc':
    print(letter.upper())
    

for item in [[1, 2, 3], [4, 5, 6]]:
    print(item[0])  
    
    
x = [len(item) for item in ['abc', 'def', 'ghi']]
print(x)

y = [i * 2 if i > 0 else 0 for i in [1, -2, 10]]
print(y)

def foo(*args):
    return len(args)
print(foo(1, 2, 4))

# def foo(x):
#     return x ** 2
# print(foo("Hello"))

# def foo(a = 1, b = 'John'):
#     return a + b
# foo()

def foo(a = 1, b = 2):
    return a + b
price = foo(b = 4)


