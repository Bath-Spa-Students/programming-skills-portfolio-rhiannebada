## Python function checking if a number is prime or not

def prime(number):
    if number <= 1: #prime numbers are greater than 1
        return False
    else:
        for i in range(2, int(number**0.5) + 1): #check for factors 2 to square root
            if number % i == 0:
                return False #if there's a factor, it's not a prime number
            return True #if there's no factors but 1 and the number itself, it is a prime number

number = int (input("Enter a number: ")) #take from user input value to calculate

#check primality and output result
if prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")