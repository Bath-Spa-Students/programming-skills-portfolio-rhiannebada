#Exercise 5: USB Shopper : A girl heads to a computer shop to buy some USB sticks. 
#She loves USB sticks and wants as many as she can get for £50. They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left. You will to use the arithmetic operators to complete this exercise.

cash = 50
price = 6
quantity = cash//price
print (f"She can buy", quantity, "USB sticks.")
change = cash%price
print (f"She will have a change of £", change, ".")