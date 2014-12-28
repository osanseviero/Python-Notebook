# Program 33. Application of what we've learned
from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number")
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You geedy bastard!")

def bear_room():
	print "There is a bear here."
	print "It has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input(">> ")
		
		if choice == "take honey":
			dead("The bear slaps in your face.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:	
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "What?"

def cthulhu_room():
	print "Here you see the great evil Cthulhu"
	print "He stares and goes insane"
	print "Do you flee or eat you head?"
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well...that was tasty")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit()

def start():
		print "You're in a dark room"
		print "There's a door at your right and one at your left."
		print "Which one do you take?"
		choice = raw_input("> ")
		if choice == "left":
			bear_room()
		if choice == "right":
			cthulhu_room()
		else:
			dead("You walk in the room until you starve.")
start()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
			
			
			
			
			