## Exercise 6: Shrinking Guest List 

guests = ["Jewel", "Anne", "JR"]
for i in guests:
    print ("Hi,", i + "! Would you like to have dinner with me this coming Tuesday?")

name = guests[2]
print ("\nSorry,", name, "won't be available that day.\n")

#JR is not available on Tuesday night
del (guests[2])
guests.insert (2, "Eriel")

#Reprint invitations
for i in guests:
    print ("Hi,", i + "! Would you like to have dinner with me this coming Tuesday?")

#Table won't arrive on time; only have space for two people
print ("\nMy apologies, I can only invite two people for dinner.")
name = guests.pop()
print ("My apologies,", name, "there's no more seats left at the table.\n")

#Invite two people
name = guests [0]
print (name + ", please come to dinner.")
name = guests [1]
print (name + ", please come to dinner.\n")

#Empty list
del (guests [0])
del (guests [0])

print (guests)