hours = float(input("Enter the hours"))
rate  = float(input("Enter the rate"))

if hours > 40:
    pay = hours*1.5*rate
    print(pay)
else:
    pay1 = hours * rate
    print(pay1)    