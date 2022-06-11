# looping using for loop
# Initially python  reads the first line of the loop and retrives
# the first name oin the list and stores in the variable name and
# reads the next line 
magicians = ['Alice', 'David', 'Charlie']
for magician in magicians:
    print(magician)
#Adding the new line using methods

magicians = ['Alice', 'David', 'Charlie']
for magician in magicians:
    print(magician.title()+", is a great magician")
    print("I cant wait to see the next  trick "+ magician.title())
print("Thank you, for visiting the show")