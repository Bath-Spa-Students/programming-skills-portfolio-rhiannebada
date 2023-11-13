## Merging dictionaries

#two different dictionaries
dictionary1 = {'Full Name':'Rhianne Ghernelle Intal Bada',
           'Age': '19', 'Birthdate': 'October 02, 2004'}
dictionary2 = {'Phone Number': '0562052633',
           'Address': 'Al Nahda, Sharjah, UAE'}

print ("First dictionary:", dictionary1, "\n")
print ("Second dictionary:", dictionary2, "\n")

#merge both, using update()
merged_dictionary = dictionary1.copy() #copy() avoids modifying the original dictionary1
merged_dictionary.update(dictionary2)

#print merged version
print ("Merged dictionary:", merged_dictionary, "\n")