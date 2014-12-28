# Program 30. Loops and lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#Printing a list
for element in the_count:
	print element

for element in fruits:
	print "I got a fruit of type %s" % element

#Mixed lists
for element in change:
	print "We can always use %r" % element
	
empty_lists = []
for i in range(0,6):
	print "Adding %d to the list:" % i
	empty_lists.append(i) 	#Here we add i to the list
	
for i in empty_lists:
	print "Element was %d" % i 