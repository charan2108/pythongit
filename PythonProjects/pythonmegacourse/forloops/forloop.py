# temperatures = [10,50,10,36,48]
# for temperature in temperatures:
#     print(temperature)

# colors = [11, 34, 98, 43, 45, 54, 54]
# for color in colors:
#     print(color)    

# colors = [11, 34, 98, 43, 45, 54, 54]
# for color in colors:
#     if color > 50:
#         print(color)    
        
# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
# for color in colors:
#     if isinstance(color, int):
#         print(color)       
             
# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
# for color in colors:
#     if isinstance(color, int) and color >50:
#         print(color)            

def cel_to_kelvin(cel):
    return cel + 273.15
for temperature in [23.5,43.5,63.5]:
    print(cel_to_kelvin(temperature))
