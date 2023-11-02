## Exercise 5: USB Shopper

#calculation using division
cash = 50
price = 6
quantity = cash//price #use of // to get result as whole number

#calculate how many USB sticks can be bought
print (f"She can buy", quantity, "USB sticks.") #use of f-string for formatted string literals

#calculate how much money will be left
change = cash%price

print (f"She will have a change of £", change, ".")
