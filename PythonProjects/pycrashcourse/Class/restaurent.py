class Restaurent:
    def __init__(self,name,cuisine,specialization, experience):
        self.name = name
        self.cuisine = cuisine
        self.specialization = specialization
        self.experience = experience        
    def describe_restaurent(self):
        print(self.name.title()+" is the name of the restaurent")    
        print(self.cuisine.title()+" is the name of the cuisine")
        print(self.specialization.title()+" is the name of the cuisine")
        print(self.experience()+" is the name of the cuisine")
    def open_restaurent(self):    
        print(self.name.title()+" is open")
        
my_restaurent = Restaurent('Seagold', 'Indian','Kebabs', 34)
print("restaurent name is"+my_restaurent.name)
print("cusine  name is"+my_restaurent.name)
my_restaurent.describe_restaurent()
my_restaurent.open_restaurent()        