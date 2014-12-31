# Program 35. Massive review and practice
import sys

# Booleans
print "Booleans: \n"
print True and False
print False and False
print True and True
print not False
print "\n\n"

print "Assert: \n"
assert True	#Will throw an error if it is false. The condition will be tested
print "\n\n"

# Will stop the loop
print "Break: \n"
while True:
	print "This will print"
	break;
	print "This won't"
print "\n\n"

# It is a little wierd, but I kinda get 
print "Class: \n"
class MyStuff(object):	#We'll check it later
    def apple(self):
        print "I AM CLASSY APPLES!"
thing = MyStuff()
thing.apple()
print "\n\n"

# Continue: to jump to the top of the loop
print "Continue: \n"
for letter in 'hello world':
	if letter == 'o':
		continue
	print letter
print "\n\n"

# Functions from always
print "Function: \n"
def writing():
	"""This is a function"""
	print "Hello, I come from a function"
writing()
print "\n\n"

# Deleting for a list or a dictionary
print "Deleting: \n"
list = [1, 3, 5, 7, 9]
del list[0]
print list
print "\n\n"

# You already know them
print "Conditionals: \n"
print "Enter a number (1 or 2)"
choice = int(raw_input("> "))
if choice == 1:
	print "good choice"
elif choice == 2:
	print "bad choice!"
else:
	print "meh meh meh"
print "\n\n"

# Introduction to exceptions
print "Exceptions: \n"
print "Enter a number"
divide = int(raw_input("> "))
try:
	a = 10 / divide
	print a
except:
	print "Error"
finally: 
	print "I don't care!"
print "\n\n"

#Runs stuff inside the string
print "Using exec \n"	
def function(n):
	print 'a'
exec 'print "hello"'
exec 'function(5)'
exec 'print "it will work" '
print "\n\n"

# Iterations
print "Using for\n"	
count = 0
for chars in "hello sir, how are you?":
	if chars == 'a' or chars == 'e' or chars == 'i' or chars == 'o' or chars == 'u':
		count += 1
print "There are %d vowels" % count
print "\n\n"

# Global variable
print "Global variable\n"
global thisVariable 
thisVariable = "I am global"
print thisVariable
print "\n\n"

# More on booleans
print "Booleans\n"
print 3 is 4
print 2 is 2
print True == True
print not True == 3 is 4
print True or False

print "\n\n"

# Lambda functins
print "Lambda functions\n"
g = lambda x: x*2
print g(4)
print g(7)
square = lambda x: x*x
print square(4)
print "\n\n"

# More on functions
print "More functions\n"
def an_example(n):
	if n == 3:
		pass
		print "Pass does nothing"
	elif n == 4:
		print "Hey there"
an_example(3)
an_example(4)	
print "\n\n"












