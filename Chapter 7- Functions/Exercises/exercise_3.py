## Exercise 3: T-Shirt 

#Description of the t-shirt to be made (size and message printed)
def make_shirt(size, message):
    print ("The t-shirt to be made will be in size", size+".")
    print ("The t-shirt will have a text printed saying, '"+message+"'\n")

make_shirt ('medium', 'I love Python!') #using positional argument 
make_shirt (message='Hello World!', size="medium") #using keyword argument