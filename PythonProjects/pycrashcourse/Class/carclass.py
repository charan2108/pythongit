class Car:
    def __init__(self,name,model,year):
        self.name = name    
        self.model = model
        self.year = year
        self.odometer = 0
    def car_name(self):
        name = (self.name+" "+self.model+""+str(self.year)) 
        return name
    def read_odometer(self):
        print("the odometer has a reading of"+str(self.odometer))
    
    def update_odometer(self, mileage):
            
my_car = Car('Mercedes','sports', 2020)
print(my_car.car_name())       
my_car.read_odometer()        