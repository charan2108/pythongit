def make_pizza(size, *toppings):
    print("\n the following size pizza "+str(size)+" inches pizza is required")
    for topping in toppings:
        print("- "+ topping)
make_pizza(16, 'Pepperoni')        
make_pizza(32, 'Pepperoni', 'Cheese', 'Macroni', 'Arcitas')        