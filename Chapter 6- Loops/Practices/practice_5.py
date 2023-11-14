## Print largest number from input number/s

largest = 0 #variable to store largest number

while True:
    number = float(input("Enter a number (0 to exit): ")) #assign values to variables from user input

    if number == 0: #checks if input is '0'
        break #exits loop if '0' is entered

    if largest==0 or number>largest: #checks if input number is larger than current largest number
        largest = number #updates largest number
#prints largest number 
if largest != 0:
    print (f"Largest number entered: {largest}") 
else:
    print ("No valid number entered.") #if no valid input before '0'