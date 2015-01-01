# Program 36. More lists

ten_things = "Apples Oranges Crows Telephones Light Sugar"
print "We need more things to get 10 things"

#Converting string to list
stuff = ten_things.split(' ')
more_stuff= ["day", "night", "song", "frisbee", "icecream", "banana", "boy", "girl"]


while len(stuff) != 10:
	next_item = more_stuff.pop()
	print "We'll add", next_item
	stuff.append(next_item)
	print "now we have %d items" % len(stuff)
	
print "We're done: ", stuff

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print ' '.join(stuff[3:5])