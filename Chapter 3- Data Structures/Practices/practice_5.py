## Finding index of a value and replace with a different value

#find value 20 in the list
list1 = [5,10,15,20,25,50,20]

print ("original list:", list1)

if 20 in list1:
    print ("20 is present in the list\n")

#find index of the first occurrence of 20
    index20 = list1.index (20)

#replace index value with 200
    list1[index20] = 200

print ("new list:", list1)