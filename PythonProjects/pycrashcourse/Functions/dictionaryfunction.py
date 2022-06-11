def profile(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
per_profile = profile('joke', 'slater')
print(per_profile)

def profile(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
per_profile = profile('joke', 'slater',age=30)
print(per_profile)
