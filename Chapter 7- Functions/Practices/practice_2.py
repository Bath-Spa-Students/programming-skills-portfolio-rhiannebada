## Python function calculating factorials

def factorial (n):
    if n == 0 or n == 1: #base case
        return 1
    else:
        return n * factorial(n-1) #recursive case
    
number = int(input("Enter a positive integer: ")) #take to-calculate value from user input
result = factorial(number) 
print (f"The factorial of {number} is {result}.") #display results