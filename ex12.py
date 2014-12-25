#Program 12. Using raw_input in a more complex way

#We ask an input
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh? ")

#Python style only uses up to 80 characters in one line
print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)