## Area of circle

def calculate_area(radius):
    pi = 3.1416 #define value of pi; approximate value
    area = pi * radius**2 #formula of circle area: pi * radius^2
    return area

#take from user input value to calculate
radius = float(input("Enter measurement of radius: ")) 

#call function with value of radius
area_of_circle = calculate_area(radius)

#display calculated area
print (f"The area of a circle with radius {radius} is {area_of_circle:.2f}.") #use of ':.2f' to round result to two decimal places