## Exercise 4:

#list of sandwich orders
sandwich_orders = ['grilled turkey sandwich' , 
          'ham sandwich', 'egg sandwich', 
          'apple peanut butter sandwich', 
          'toasted sandwich', 'bbq chicken sandwich']

finished_sandwiches = [] #empty list

while sandwich_orders:
    current_order = sandwich_orders.pop() #will remove from list
    print ("I made your", current_order.title() + ".")
    finished_sandwiches.append(current_order) #will be added to the other empty list

print ("") #space for separation

for finished_sandwich in finished_sandwiches: 
    print (finished_sandwich.title(), "is done and ready!") #title() for uppercasing initials