## Exercise 4: Rivers

#assigning value to key
rivers = {"nile" : "egypt",
          "yangtze" : "eurasia",
          "mississippi" : "the united states"}

#using loop, print a sentence for each river
for river, country in rivers.items():
    print ("The", river.title(), "runs through", country.title() + ".")  # title() is used to change initials to uppercase and the rest lowercase

print ("\n")

#print the name of each river included in the dictionary
print ("Rivers:")
for river in rivers.keys():   #keys() display all keys in a dictionary
    print (river.title())

print ("\n")

#print the name of each country included in the dictionary
print ("Countries the rivers run through:")
for country in rivers.values():   #values() display all values in a dictionary
    print (country.title())