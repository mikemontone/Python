toppings = []

#prompt = "\nPlease tell me what toppings you want on your sandwich: "
#prompt += "\n (Enter 'quit' when you are finished adding toppings.) "

#while True:
#   topping = input(prompt)

#   if topping == 'quit':
#       break
#   else:
#       print("Adding " + topping + " to your sandiwch.")

def make_sandwich(*toppings):
    """ accepts toppings to make a sandwich, displays the toppings ordered. """
    topping = input("Topping: ")
    print("\nMaking you sandwich with the following toppings: ")
    for topping in toppings:
        print("-" + topping)

make_sandwich()
#make_sandwich('turkey','cheddar','pork roll','dijon aioli')


