## Break statement

numbers = [2,4,8,10,13,3,6,9]

print ("List of numbers:", numbers)
#loop through the list of numbers
for number in numbers:
    print ("Current number:", number)

    #breaks loop when number 3 is found   
    if number == 3:
        print ("Number 3 is present in the list.")
        break

print ("Loop finished.")