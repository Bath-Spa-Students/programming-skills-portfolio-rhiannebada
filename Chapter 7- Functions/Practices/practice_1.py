## Python function

def add_numbers(a,b): #function 'add_numbers' taking 2 parameters 'a' and 'b'
    return a + b #return sum of 'a' and 'b'

#take two numbers from user input
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

result = add_numbers(number1, number2) #store results

#outputs sum of two input numbers
print (f"The sum of {number1} and {number2} is: {result}")