# Program 29. Nested ifs 

print "You pick a map. You can go to the Garghastan Tower (1) or to the Malivolent Valley (2)"
place = raw_input("> ")

if place == "1":
	print "A guard welcomes you."
	print "You go up in the tower."
	print "You sense something is wrong"
	print "Your master is in the ground, bleeding."
	print "The Black Wizard is there!"
	print "Do you take your staff (1) or your sword (2)?"
	weapon = raw_input("> ")
	
	if weapon == "1":
		print "You take out your staff and shout \"Expeliarmus!\""
		print "Then you throw a fireball at the Black Wizard."
		print "Black Wizard escaped!"
		print "End 1"
		
	elif weapon == "2":
		print "You take out your sword"
		print "You run to attack the Black Wizard."
		print "Your sword melt. That Wizard D:!"
		print "You take out your staff...too late"
		print "A lighting hits you, you're dead"
		print "End 2"

elif place == "2":
	print "A wild troll appears!"
	print "You attack the trol."
	print "Trol kills you."
	print "End 3"

else:
	print "You self-destruct"
	print "End 4."















