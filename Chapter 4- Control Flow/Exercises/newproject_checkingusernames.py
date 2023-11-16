## Exercise 8: Checking Usernames
 
#list of current users
current_users = ['rhianne', 'sam', 'wyxy', 'aliyah', 'jungwon', 'jake', 'sunoo']
#list of current users
new_users = ['JUNGWON', 'niki', 'yasmine', 'Jake', 'rj']

#convert to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users: #check if new username exist in current list
        #output if new username already exists
        print ("Sorry,", new_user, "is already taken as a username.")   
    else:
        #output if new username doesnt exist and available
        print ("Excellent!", new_user, "username is still available.")

