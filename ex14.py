#Program 14. Prompting and Passing
from sys import argv

#Run it as python ex14.py osan pass (you can change this last two variables)

#We assign the script to the name of the document (ex14.py), user_name to the first variable (osan) and password to the third variable (pass)
script, user_name, password = argv

prompt = '>\t'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)	#We ask an input and then print the variable prompt

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

print """
Username = %r 
Password = %r
City = %r
Computer = %r 
""" % (user_name, password, lives, computer)