#Program 5. Printing and variables

name = 'Omar'
age = 18
height = 181
height_inches = height / 2.54
weight = 60
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print "My name is %s." % name
print "I am %d cm tall and %d inches tall." % (height, height_inches)
print "I am %d kg heavy." % weight
print "I have %s eyes and %s hair." % (eyes, hair)

print "If I add %d, %d, and %d I get %r." % (
age, height, weight, age + height + weight)

number = 1.538
print "%s rounded is %d." % (number, round(number))