## Exercise 7: Favorite Places

#list of names and their favorite places
fav_places = {
    'ben': ['spain', 'hawaii'],
    'ian': ['beach', 'library', 'dubai mall'],
    'hilary': ['japan', 'tagaytay', 'south korea']
}

#print each name with their fav places
for name, places in fav_places.items():
    print("\n"+name.title(), "likes these places:")
    for place in places:
        print (">"+place.title())