#Program 6. More strings 

#String inside a string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y 
print "I said: %r." %x
print "I also said: '%s'." %y

#Using a variable as a string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

#Concatenation
w = "This is the left side of..."
e = "a string with a right side."
print w + e