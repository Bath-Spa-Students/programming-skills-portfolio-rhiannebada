## if-else statement

#assign values to variables from user input
a=float(input("Enter a number: "))

if a < 10: 
    b = 'O' #will assign 'O' to 'b' if 'a' is less than 10
else:
    b = 99 #will assign '99' to 'b' if 'a' is equal or more than than 10

print ("The value of b is:", b)