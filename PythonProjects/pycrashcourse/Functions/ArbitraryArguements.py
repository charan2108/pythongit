def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')    
make_pizza('pepperoni', 'cheese', 'macroni')   


def make_pizza(*toppings):
    print("\n Need pizza with the following  toppings")
    for topping in toppings:
        print("- " + topping) 
make_pizza('Pepperoni')        
make_pizza('Pepperoni', 'Macroni','Cheese', 'Yogurt')        