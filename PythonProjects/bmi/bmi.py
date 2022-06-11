weight = float(input("Enter your weight in kgs"))
height = float(input("enter height in meters"))
    
bmi = (weight)/(height)**2
print(bmi)
    
if bmi <18.5:
    print("Underweight")
elif bmi <=25:
    print("Normal")
elif bmi <=29:
    print("Overweight")
elif bmi >=29:
    print("Obese")
else:
    print("None")
    