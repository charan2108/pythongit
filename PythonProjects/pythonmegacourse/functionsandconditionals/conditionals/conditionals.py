# def mean(value):
#     if type(value) == dict:
#         the_mean=sum(value()/len(value))
#     else:
#         the_mean=sum(value()/len(value))  
    
#     return the_mean
# student_grades = {'Mike': 9.5, "Sim": 8.5, 'mat':85}
# print(mean(student_grades))

# def  temperature(degree):
#     if degree >7:
#         print('Warm')
#     elif degree <=5:
#         print('Cold')
#     else:
#         print('None')
# temperature(15)                

# def  string(password):
#     if password > '8':
#         return True
#     else: 
#         return False
# string('Terminator')        

# a = -10
# if a * 2 > a:
#     print("Greater")
# else:
#     print("Less or equal")    
    
# def foo(x, array):
#     if x in array:
#         return True
#     else:
#         return False
 
# print(foo(1, [1, 2, 3]))
# print(foo(1, [2, 3]))
# print(foo(1, ['1', 2, 3]))    

def  temperature(degree):
    if degree >=25:
        print("Hot")
    elif degree >= 15 and degree <= 25:
        print("Warm")
    elif degree <=15:
        print("Cold")    
    else:
        print("None")
temperature(15)        
                
