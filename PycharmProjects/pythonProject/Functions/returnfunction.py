def name(first_name, last_name):
    full_name = first_name+' '+last_name
    return full_name.title()
abbrevation = name('Alfa','chaplin')
print(abbrevation)

# optional
def name(first_name, middle_name, last_name):
    full_name = first_name+' '+middle_name+' '+last_name
    return full_name.title()
abbrevation = name('Alfa','charlie','chaplin')
print(abbrevation)

def name(first_name, last_name, middle_name=" "):
    if middle_name:
        full_name = first_name + " " +middle_name + " "+last_name
    else:
        full_name = first_name+ " " + last_name
    return full_name.title()
alto = name('Alfa', 'charlie')
alto =name('Alfa', 'Charlie', 'Chaplin')
print(alto)
