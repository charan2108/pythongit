# height =float(input("Enter your height in m:"))
# weight =float(input("Enter your height in kg:"))

# bmi = (weight)/(height/100)**2
# print(bmi)

# if bmi <=18:
#     print("Underweight")
# elif bmi>=18 and  bmi<=25:
#     print("Normal weight")
# elif bmi>=25 and bmi<=29:
#     print("Overweight")
# elif bmi<=29 and bmi>=30:
#     print("Obesity")
# else:
#     print("Visit the consultant")            
        
    
height =float(input("Enter your height in m:"))
weight =float(input("Enter your weight in kg:"))

bmi = int(weight)/float(height)**2
print(bmi)

if bmi <=18:
    print("Underweight")
elif bmi>=18 and  bmi<=25:
    print("Normal weight")
elif bmi>=25 and bmi<=29:
    print("Overweight")
elif bmi<=29 and bmi>=30:
    print("Obesity")
else:
    print("Visit the consultant")  