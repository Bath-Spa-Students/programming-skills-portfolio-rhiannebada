## Nested decision

##assign values to variables from user input
amount1 = float(input("Enter a number greater than 10: "))
amount2 = float(input("Enter a number less than 100: "))

#both should meet conditions, thus with the use of 'and'
if amount1 > 10 and amount2 < 100:
        if amount1 > amount2: #comparing if both meet the conditions
            print ("\nAmount #1 (", amount1, ") is greater than", "Amount #2 (", amount2, ")." )
        elif amount2 > amount1:
            print ("\nAmount #2 (", amount2, ") is greater than", "Amount #1 (", amount1, ")." )
        else:
             print ("\nAmount #1 (", amount1, ") and", "Amount #2 (", amount2, ") are equal." )
else:
    print ('Conditions are not met to compare amounts.') #output if conditions were not met
        