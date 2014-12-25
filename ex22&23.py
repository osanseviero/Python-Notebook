# Program 22 & 23. Becoming better at this. 
# Today we will learn a set of tips to become a better python programmer

# Rule 1. Be straightforward.
	#In program 18, we did it two ways.
	#Which one of this is straightforward?
	
def print_two(*args):	
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_two_again(arg1, arg2):	
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Rule 2. One thing at a time
print 'one'; print 'two'	#This is ok and will run, but this is better:
print 'one'
print 'two'

# Rule 3. Lines should have a max length of 80 lines (except import or URL)

# Rule 4. Don't use parenthesis when don't needed. 
	#We'll see later the conditionals, but here is an example of bad work
def add(a, b):
	return ( a + b )
	
# Rule 5. Always ident 4 spaces (not 2 or 8)

# Rule 6. Import each thing in a different line

# There are many rules, but I won't go over each of them right now.

# Now let's read some code from the .py files from this projects
	# https://github.com/gleitz/howdoi
		# https://github.com/gleitz/howdoi/blob/master/howdoi/howdoi.py
			# Concepts used: Importing, conditionals, functions















