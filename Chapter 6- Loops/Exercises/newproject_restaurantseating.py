## Exercise 7: Restaurant Seating

#ask user how many people are in their dinner group
persons = int(input("Enter how many people are in your dinner group: "))

if persons > 8:
    print ("Sorry, you'll have to wait for a table.")
else:
    print ("Your table is ready.")