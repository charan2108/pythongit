# positional arguements
def make_shirt(shirt_type, size):
    print("i have shirt size "+shirt_type+" . ")
    print("the size of the shirt is"+size.title()+"!")
make_shirt('t-shirt', 's')


def make_shirt(shirt_type, size):
    print("i have shirt size "+shirt_type+" . ")
    print("I love python size is"+size.title()+"!")
make_shirt(shirt_type = 'Formals', size='Large')
make_shirt(size='Large', shirt_type = 'Formals')
def make_shirt(shirt_type, size):
    print("i have shirt size "+shirt_type+" . ")
    print("I love python size is"+size.title()+"!")
make_shirt(shirt_type = 'Formals', size='Medium')
make_shirt(size='Large', shirt_type = 'Formals')
    