#calculating average

#input course marks
cd1 = (int(input("Enter your marks in Code Lab 1: ")))
dst = (int(input("Enter your marks in Digital Storytelling: ")))
dvd = (int(input("Enter your marks in Digital Visual Design: ")))

sum = cd1+dst+dvd
average = sum / 3 #3 for 3 courses
percentage = (sum/300)*100 #300 for 100 per course

print ("\nAverage:", average)
print ("\nPercentage:", percentage)