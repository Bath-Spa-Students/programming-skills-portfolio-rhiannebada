## Exercise 6: Hello Admin
 
#list of usernames
usernames = ['rhianne', 'ghernelle', 'rhi', 'anne', 'admin']

for username in usernames:
    if username == 'admin':
        #print if username is 'admin'
        print ("Good day admin, would you like to see a status report?")
    else:
        #print general statement to all usernames not 'admin'
        print ("Good day", username + ", thank you for logging in.")