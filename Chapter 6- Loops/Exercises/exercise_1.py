## Exercise 1: Pizza Toppings

#asks user/s to input elements
pizza = "\n What topping would you like to include on your pizza?"
pizza += "\n Enter/type 'quit' when done:" #user will have to enter the word "quit" to end the program

while True:
    topping = input (pizza)
    if topping != 'quit': #any input not spelled as "quit" will display the following
        print (" Will proceed to add", topping , "to your pizza.")
    else:
        break 