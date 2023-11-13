## Exercise 4: Large Shirts 

#Description of the t-shirt to be made
def make_shirt(size='large', message='I love Python!'):
    print ("The t-shirt to be made will be in size", size+".")
    print ("The t-shirt will have a text printed, saying '"+message+"'\n")

make_shirt () #default size and message
make_shirt (size='medium') #medium size, default message
make_shirt ('small', 'Hello World!') #any size, different message
