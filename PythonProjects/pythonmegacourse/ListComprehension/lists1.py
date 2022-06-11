temps =[100,200,300,400]
new_temps=[]
for temp in temps:
    new_temps.append(temp/10)
print(new_temps)    

temps =[120,200,300,400]
new_temp = [temp/10 for temp in temps]
print(new_temp)

temps =[120,200,300,400]
new_temp = [temp/10 for temp in temps if temp != -9999]
print(new_temp)
# exercise
def dum(list):
    return[a for a in list if isinstance(a,int)]

temps =[120,200,300,400]
new_temp = [temp/10 if temp != -9999 else 0 for temp in temps  ]
print(new_temp)