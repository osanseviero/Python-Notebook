#Program 19. More complex functions
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "That's enough"
	print "Get a blanket.\n"
	
print "We can give the values:"
cheese_and_crackers(20, 30)

print "We can also use our own values"
amount_of_cheese = 100
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math in here!"
cheese_and_crackers(10 + 20, 5 + 6)

print "And math with variables"
cheese_and_crackers(amount_of_cheese + 5, amount_of_crackers + 5)

