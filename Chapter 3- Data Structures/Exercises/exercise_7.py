## Exercise 7: Seeing the World 

#list of places I want to visit
places = ['South Korea', 'Palawan', 'Japan', 'Maldives', 'Switzerland']

print ("\nOriginal order:")
print (places) #will print exact same order as in the list

print ("\nAlphabetical order using sorted():")
print (sorted(places)) #will print list in alphabetical order using sorted()

print ("\nOriginal order:")
print (places)

print ("\nReversed Alphabetical order using sorted():")
print (sorted(places, reverse=True)) #will print list in reversed alphabetical order using sorted()

print ("\nOriginal order:")
print (places)

print ("\nReversed order using reverse():")
places.reverse() #will print list in reversed order using reverse()
print(places) 

print ("\nOriginal order using reverse():")
places.reverse() #will print exact same order as in the list using reverse()
print (places)

print ("\nAlphabetical order using sort():")
places.sort() #will print list in alphabetical order using sort()
print (places) 

print ("\nReversed Alphabetical order using sort():")
places.sort(reverse=True) #will print list in reversed alphabetical order using sort()
print (places)