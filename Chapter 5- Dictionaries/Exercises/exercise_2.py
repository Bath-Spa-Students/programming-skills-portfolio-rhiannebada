## Exercise 2: Glossary 

#assigning value to key
glossary = {"BIT /bɪt/" : "the individual 1's and 0's you see in binary",
            "FUNCTION /ˈfʌŋ(k)ʃn/" : "a block of code that can be referenced by name to run the code it contains",
            "INPUT /ˈɪnpʊt/" : "any interaction from the user to the program",
            "STRING /strɪŋ/" : "reffered as variables holding words",
            "VARIABLE /ˈvɛːrɪəbl/" : "a container that holds a single number, word, or other information that you can use throughout a program"}

print ("BIT /bɪt/") 
print ("\t" + ":" + (glossary ["BIT /bɪt/"])) #use of \t to indent definitions

print ("\nFUNCTION /ˈfʌŋ(k)ʃn/") #use of \n to add blank line
print ("\t" + ":" + (glossary [ "FUNCTION /ˈfʌŋ(k)ʃn/"]))

print ("\nINPUT /ˈɪnpʊt/")
print ("\t" + ":" + (glossary ["INPUT /ˈɪnpʊt/"]))

print ("\nSTRING /strɪŋ/")
print ("\t" + ":" + (glossary ["STRING /strɪŋ/"]))

print ("\nVARIABLE /ˈvɛːrɪəbl/")
print ("\t" + ":" + (glossary ["VARIABLE /ˈvɛːrɪəbl/"]))