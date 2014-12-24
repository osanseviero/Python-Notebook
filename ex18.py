#Program 18. Functions

#First Function
def print_two(*args):	#List of arguments
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#Second Function
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
#Dedenting
	
#Third function
def print_one(arg1):
	print "arg1: %r" % arg1

#Fourth function
def print_none():
	print "I got nothin'."

print_two("My name is", "Osan")
print_two_again("My name is", "Osan")
print_one(":)")
print_none()