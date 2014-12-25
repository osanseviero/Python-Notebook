#Program 5. Printing and variables

#Declarin variables
name = 'Osan'
age = 18
height = 181
height_inches = height / 2.54
weight = 60
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

# We use %s for strings and %d for digits (integers)
print "My name is %s." % name
print "I am %d cm tall and %d inches tall." % (height, height_inches)
print "I am %d kg heavy." % weight
print "I have %s eyes and %s hair." % (eyes, hair)

# %r Will give you raw data.
print "If I add %d, %d, and %d I get %r." % (
age, height, weight, age + height + weight)

# Using the round function
number = 1.538
print "%s rounded is %d." % (number, round(number))