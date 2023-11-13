## Exercise 5: Cities

#Describe a city
def describe_city(city, country='Philippines'):
    sentence = city.title() + " is in " + country.title()+"." #use of title() to display text in capitalisation
    print (sentence)

#3 different cities, 1 is not in default country
describe_city ('manila')
describe_city ('cebu')
describe_city ('seoul', 'south korea')
    