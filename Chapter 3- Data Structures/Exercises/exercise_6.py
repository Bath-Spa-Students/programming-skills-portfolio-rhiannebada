## Exercise 6: Shrinking Guest List 

#list of people to invite
names = ["Jewel", "Anne", "JR", "RJ"]
print ("Hi,", names [0] + "! Would you like to have dinner with me this coming Tuesday?") #will print a message inviting someone from the list
print ("Hi,", names [1] + "! Would you like to have dinner with me this coming Tuesday?")
print ("Hi,", names [2] + "! Would you like to have dinner with me this coming Tuesday?")
print ("Hi,", names [3] + "! Would you like to have dinner with me this coming Tuesday?")

#one guest can't make it to dinner
name = names[2]
print ("\nSorry,", name, "won't be available that day.\n") 

#JR is not available on  Tuesday night
del (names[2]) #will delete JR in the list
names.insert (2, "Eriel") #will be added to the list in replace to JR

#reprint invitations
print ("Hi,", names [0] + "! Would you like to have dinner with me this coming Tuesday?") #will print a message inviting someone from the list
print ("Hi,", names [1] + "! Would you like to have dinner with me this coming Tuesday?")
print ("Hi,", names [2] + "! Would you like to have dinner with me this coming Tuesday?")
print ("Hi,", names [3] + "! Would you like to have dinner with me this coming Tuesday?")

#Table won't arrive on time; only have space for two people
print ("\nMy apologies, I can only invite two people for dinner.")
name = names.pop() #will remove guest from the list
print ("\tMy apologies,", name, "there's no more seats left at the table.") #print an apology message
name = names.pop()
print ("\tMy apologies,", name, "there's no more seats left at the table.\n")

#Invite remaining two guest in the list
name = names [0] 
print (name + ", please come to dinner.")
name = names [1]
print (name + ", please come to dinner.\n")

#Empty list
del (names [0])
del (names [0])

print (names) #to check if the list is empty