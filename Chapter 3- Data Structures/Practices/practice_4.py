## Transfer elements from one list to another

#2 different lists of numbers
numbers1 = [1,2,3,4,5,6,7,8,9,10]
numbers2 = [] #empty list

print ("list 1:", numbers1)
print ("list 2:", numbers2)

for i in numbers1:
    numbers2.append(i) #elements in list numbers1 will trnasfer to list numbers2

print ("list 1:", numbers1)
print ("new list 2:", numbers2) #will print new list numbers2