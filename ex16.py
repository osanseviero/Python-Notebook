#Program 16. Writing files
from sys import argv

#Run it with text16.txt

script, filename = argv

print "Hello\nWe are going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')	#The w is to tell we want to write on it

print "Truncating the file..."
target.truncate()

print"Now I'll ask you two lines"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Let's write it in the file"
target.write(line1 + "\n" + line2 + "\n")	#Concatenating
target.write(line3 + "\n")

print "And we close it"
target.close()
print "And we will read it now"
target = open(filename, 'r')	#The r is to tell we want to read it
print target.read()
