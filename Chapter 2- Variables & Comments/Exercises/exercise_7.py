## Exercise 7: File Extension

#assign the filename
filename = 'python_notes.txt'
print ("Filename:", filename)

#remove file extension using removesuffix()
filename_without_extension = filename.removesuffix('.txt')

#print filename without file extension
print ("Filename without file extension:", filename_without_extension) #should output 'python_notes'