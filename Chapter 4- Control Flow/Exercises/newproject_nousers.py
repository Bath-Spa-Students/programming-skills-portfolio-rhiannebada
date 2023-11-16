## Exercise 7: No Users

#non-empty list version
#list of usernames
usernames = ['rhianne', 'ghernelle', 'rhi', 'anne', 'admin'] 
print ("Non-empty list version:")

if usernames:
    for username in usernames:
        if username == 'admin':
            #print if username is 'admin'
            print ("Good day admin, would you like to see a status report?")
        else:
            #print general statement to all usernames not 'admin'
            print ("Good day", username + ", thank you for logging in.")
else: 
    #print if list is empty
    print ("We need to find some users!")


#empty list version
usernames = [] #empty list
print ("\nEmpty list version:")

if usernames:
    for username in usernames:
        if username == 'admin':
            #print if username is 'admin'
            print ("Good day admin, would you like to see a status report?")
        else:
            #print general statement to all usernames not 'admin'
            print ("Good day", username + ", thank you for logging in.")
else: 
    #print if list is empty
    print ("We need to find some users!")

