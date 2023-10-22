## Exercise 5: Change Guest List

guests = ["Jewel", "Anne", "RJ", "JR"]
for i in guests:
    print ("Hi,", i + "! Would you like to have dinner with me this coming Tuesday?")

name = guests[3]
print ("\nSorry,", name, "won't be available that day.\n")

#JR is not available on  Tuesday night
del (guests[3])
guests.insert (3, "Eriel")

#Reprint invitations
for i in guests:
    print ("Hi,", i + "! Would you like to have dinner with me this coming Tuesday?")

