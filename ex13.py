#Program 13. Importing
#Run "python ex13.py first second third", you are sending the variable

from sys import argv	#You import a module or library

script, first, second, third = argv #Unpacking

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is: ", third