## Exercise 5: No Pastrami

#list of sandwich orders
sandwich_orders = ['pastrami sandwich',
              'grilled turkey sandwich' , 
              'ham sandwich', 'pastrami sandwich',
              'egg sandwich', 'apple peanut butter sandwich', 
              'toasted sandwich', 'pastrami sandwich', 
              'bbq chicken sandwich', 'pastrami sandwich']

finished_sandwiches = [] #empty list

print ("The deli has run out of pastrami.")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove ('pastrami sandwich') #will remove all pastrami orders from list

print ("") #space for separation

while sandwich_orders:
    current_order = sandwich_orders.pop() #will remove from list
    print ("I made your", current_order.title() + ".")
    finished_sandwiches.append(current_order) #will be added to the other empty list

print ("")

for finished_sandwich in finished_sandwiches: 
    print (finished_sandwich.title(), "is done and ready!") #title() for uppercasing initials

print ("")

print ("Sandwich Orders:")
print (finished_sandwiches) #to check if all pastrami orders were removed