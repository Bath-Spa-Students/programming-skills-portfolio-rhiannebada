## elif statement to determine the season based on the month

#assign values to variables from user input
month = (input("Enter month: "))

#checks input to determine season
if month.lower() in ['december', 'january', 'february']:
    season = 'Winter' #Winter is from month of december to february

elif month.lower() in ['march', 'april', 'may']:
    season =  'Spring' #Spring is from month of march to may

elif month.lower() in ['june', 'july', 'august']:
    season =  'Summer' #Summer is from month of june to august

elif month.lower() in ['september', 'october', 'november']:
    season =  'Autumn' #Autumn/Fall is from month of september to november

else :
    season = "\nEntered month is invalid." #output if input is not a month/wrong spelling/in other type

print (f"\nThe season for {month.capitalize()} is {season}.")