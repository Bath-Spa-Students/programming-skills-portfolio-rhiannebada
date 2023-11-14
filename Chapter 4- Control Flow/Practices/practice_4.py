## if-else statement that displays whether speed is normal/abnormal

#assign values to variables from user input
speed = float(input("Enter speed: "))

if speed >= 24 and speed <= 56: #checks if value is within the range of 24-56
      print ("\nSpeed (", speed, ") is normal.") #output if value is within range

else:
     print ("\nSpeed (", speed, ") is abnormal.") #output if value is outside range