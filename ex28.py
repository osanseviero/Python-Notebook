#Program 28. Else statements

people = 30
cars = 40
trucks = 15

if cars > people:
	print "We should take the cars."
elif cars > people:
	print "We shouldn't take the cars."
else:
	print "We can't decide."

if trucks > cars:
	print "Too many trucks."
elif cars > trucks:
	print "Maybe we could take the trucks"
else:
	print "We can't decide"
	
if people > trucks: 
	print "Alright, let's just take the trucks"
else:
	print "Fine...let's stay at home"