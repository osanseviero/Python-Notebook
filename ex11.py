#Program 11. User input

#We use commas so we don't jump a line.
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#Remember, %r will give the raw data
print "So, you're %s old, %r tall and %r heavy." % (
age, height, weight)

#Trying some numbers
print "Enter a number",
number = int(raw_input())
print "The square of %d is %d" % (number, number**2)