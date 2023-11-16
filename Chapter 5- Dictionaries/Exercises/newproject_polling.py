## Exercise 6: Polling

#list of people and their favorite programming language
fav_languages = {
    'rhianne': 'python',
    'sam': 'javascript',
    'elle': 'html',
    'jake': 'c'
    }

for name, language in fav_languages.items():
    print (name.title()+ "'s favorite language is", language.title()+".")

print ("")

programmers = ['rhianne', 'jennifer', 'sam', 'elle', 'jake', 'samuel']

for programmer in programmers:
    if programmer in fav_languages.keys():
        print ("Hello", programmer.title() + ", thank you for taking the poll!")
    else:
        print ("Hello", programmer.title() + ", what's your favorite programming language?")