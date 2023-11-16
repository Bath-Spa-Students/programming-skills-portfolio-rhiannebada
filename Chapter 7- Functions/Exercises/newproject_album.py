## Exercise 7: Album

#function creating a dictionary that represents an album with artist and title
def make_album(artist, title):
    album_dictionary = {
        'Artist': artist.title(), #store artist name in title case
        'Album Title': title.title(), #store album title in title case
    }
    return album_dictionary 

#creating albums using make_album function and print
album = make_album ('enhypen', 'dark blood') #creating album for ENHYPEN
print (album)

album = make_album ('sasha sloan', 'only child') #creating album for Sasha Sloan
print (album)

album = make_album ('lyn lapid', 'to love in the 21st century') #creating album for Lyn Lapid
print (album)