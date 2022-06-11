weight =input("Enter weight in kg")
height =input("Enter height in m")

weight = int(weight)
height=float(height)

bmi = (weight)/(height*height)
bmi = int(bmi)
print(bmi)
if bmi <=18.5:
    print("Underweight")
elif bmi<=25:
    print("NormalWeight")
elif bmi<=29:
    print("Overweight")
elif bmi>=30:
    print("Obesity")
else:
    print("none")
    