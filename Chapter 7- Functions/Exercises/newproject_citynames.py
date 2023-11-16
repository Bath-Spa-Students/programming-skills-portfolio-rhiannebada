## Exercise 6: City Names

#function taking the name of the city and its coutry
def city_country(city, country):
    return city.title()+ ", " + country.title()

city = city_country('manila', 'philippines')
print (city)
city = city_country('seoul', 'south korea')
print (city)
city = city_country('doha', 'qatar')
print (city)
city = city_country('tokyo', 'japan')
print (city)
city = city_country('cebu', 'philippines')
print (city)