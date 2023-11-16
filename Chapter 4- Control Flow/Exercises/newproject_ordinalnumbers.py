## Exercise 9: Ordinal Numbers
 
#list of numbers 1-9 using range function
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print ("1st") #print 1st if number is 1
    elif number == 2:
        print ("2nd") #print 2nd if number is 2
    elif number == 3:
        print ("3rd") #print 3rd if number is 3
    else:
        print (str(number)+"th") #following numbers will print with added 'th'