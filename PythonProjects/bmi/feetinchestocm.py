height_feet = int(input("Enter the height_feet"))
height_inches = int(input("Enter the height_inches"))

height_inches += height_feet * 12
# conversion to cm units
height_cm = round(height_inches * 2.54, 1)
height_in_meters = height_cm * 0.01
print(height_in_meters)