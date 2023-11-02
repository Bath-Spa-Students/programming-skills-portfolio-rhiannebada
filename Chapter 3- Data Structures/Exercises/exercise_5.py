## Exercise 5: Change Guest List

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