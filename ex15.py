#Program 15. Reading Files
#Run it like "python ex15.py ex15_sample.txt"

from sys import argv
script, filename = argv

#Importing. This way needs us to import the name
txt = open(filename)		#Returns the file as an object				
print "Here's your file %r:" %filename
print txt.read()			#this is a method



#Asking. This way enables opening different files (the one that the user wants).
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()