# Program 37. Dictionaries

# Dictionaries: Like a list, but you can use anything to find the position of an element
states = {
	'Oregon' : 'OR',
	'Florida': 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY has: ", cities['NY']
print "OR has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']


# But we like the hard way
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Printing all abbreviation
print '-' * 10
for state, abbreviations in states.items():
	print "%s is abbreviated %s" % (state, abbreviations)

# Let's go crazy
print '-' * 10
for state, abbreviations in states.items():
	print "%s is abbreviated %s and has %s city" % (state, abbreviations, cities[abbreviations])

# Here we ask for the index Texas, and we fail. Then we assign the element Does not exist with index TX
print '-' * 10
state = states.get('Texas')
if not state:
	print "Sorry, not Texas"
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is %s" % city








































