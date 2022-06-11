height = float(input("Enter the height"))
weight = float(input("Enter the weight"))
bmi = (weight)/(height)**2
print(bmi)

if bmi<18:
    print("Underweight")
elif bmi<=25:
    print("Normal Weight")
elif bmi <=29:
    print("Overweight")
elif bmi >=30:
    print("Obesity")
else:
    print("ENd")