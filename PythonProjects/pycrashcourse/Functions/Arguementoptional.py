def name(first_name, middle_name, last_name):
    full_name = first_name+' '+ middle_name+' '+last_name
    return full_name.title()
calc = name('sachin','lee','marl')
print(calc)

def name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

cod = name('sachin','jacks')
print(cod)  
        
cod = name('sachin', 'lee','jacks')
print(cod)           