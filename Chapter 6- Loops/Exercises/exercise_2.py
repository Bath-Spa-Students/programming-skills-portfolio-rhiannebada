## Exercise 2: Movie Tickets

ticket = "How old are you?"
ticket += "\n Enter/type 'quit' when done:" #user will have to enter the word "quit" to end the program

while True:
    age = input (ticket)
    if age == 'quit':
        break
    age = int(age)

    if age < 3: #ages less that 3 will output the following
        print ("\tYou're tickets are free!")
    elif age < 13: #ages less that 13 will output the following
        print ("\tYou're ticket is $10!")
    else: #ages 13 and above will output the following
        print ("\tYou're ticket is $15!")