class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def sit(self):
        print(self.name.title()+'is now sitting here') 
    def roll(self):
        print(self.name.title()+"is rolling over there")
my_dog = Dog('Brucy', 8)
print("My dog name is"+my_dog.name.title()+"is there")
print("My dog age is "+str(my_dog.age)+".")
my_dog.sit()
my_dog.roll()               