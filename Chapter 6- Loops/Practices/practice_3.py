## Print sum of numbers 1-100 using 'for' loop

total_sum = 0 #variable to store sum

for number in range(1,101): #range from 1 to 100
    total_sum += number #adds each number to 'total_sum'

#display total sum
print ("The overall sum of all numbers from 1 to 100 is", total_sum)