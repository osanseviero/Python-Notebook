# Program 34. A game
from sys import exit
import time

def start(life, str):
	"""Introduction of the game"""
	print "Minion says: \"Welcome to Mordor, the Master is waiting\""
	print "You enter the tower"
	print "Actions: Look around (1) / Go upstairs (2)"
	choice = int(raw_input("> "))
	if choice == 1:
		print "You look at your left. Two trolls look at you"
		time.sleep(1)
		print "You look ahead. The black stairs are there, and the green, small goblin is waiting"
		time.sleep(1)
		print "You look at your right. The head of a mountain pig is in the wall"
		time.sleep(1)
		print "Minion says: \"Hurry up, the Master is waiting\""	
	print "You take the stairs"
	time.sleep(1)
	print "Minion says \"This tower has been here since the born of the black wizard\""
	time.sleep(1)
	print "\"During the last 30 years, we've been waiting the return of our hero.\""
	time.sleep(1)
	print "\"We think you're our hero\""
	time.sleep(1)
	print "You arrive the top of the tower. A small rabit is there"
	print "Minion says: \"Wait here, the master will come here soon\""
	choice = 1
	
	print "You take out your steel sword"
	print "You get closer to the rabbit"
	while choice == 1:
		print "Actions: Kill the rabbit (1) / Wait (2)"
		choice = int(raw_input("> "))
		if choice == 1:
			life -= 5
			if life >= 0:
				print "Your life is %d" % life
			if life <= 0:
				die("rabbit")
			elif life < 50:
				print "The rabbit turn into a dragon"
				print "The dragon throws a flame at you (-50HP)"
				life -= 50
			elif life < 90:
				print "The rabbit used tacklle (-10HP)"
				life -= 10
			else: 
				print "Rabbit shoots a fireball to you (-5HP)"
		else: 
			choice = 0
		
		
	print "Here is your master"
	time.sleep(1)
	print "A giant raven flies to the tower"
	time.sleep(2)
	print "The raven arrives and turns into the black wizard"
	time.sleep(3)
	print "Master says: \"Hello, student. I will teach you to use magic to defeat your enemies\""
	time.sleep(1)
	
	print "Days pass as you train"
	time.sleep(1)
	print "Actions: Go to the gym (1) / train versus an ogre (2) / train versus the minions (3)"
	choice = int(raw_input("> "))
	if choice == 1:
		print "HP increased"
		life = 150
	elif choice == 2:
		print "Strength increased"
	else:
		print "HP increased"
		print "strentgh increased"
		life = 125
		str = 2
	time.sleep(1)
	print "You continue training"
	life += 20
	print "HP: %d\nStrentgh: %d" % (life, str)
	
	time.sleep(1)
	print "Your master arrives"
	print "Master says: \"Let's see how strong you are\""
	print "ENTER FIGHT"
	hpRabbit = 100
	print "You: %d vs Rabbit: %d" % (life, hpRabbit)
	while hpRabbit >= 0 or life >= 0:
		print "Actions: Use your steel word(1)/ Use magic(2)"
		choice = int(raw_input("> "))
		if choice == 1:
			print "Your life is %d" % life
			print "Rabbit life is %d" % hpRabbit
			print "The rabbit life is %d" % life
			hit = str *10
			hpRabbit -= hit
			print "You hit the rabbit (-%d)" % hit
			print "The rabbit runs around, scared"
		elif choice == 2:
			print "Your life is %d" % life
			print "Rabbit life is %d" % hpRabbit
			hit = str * 20
			hpRabbit -= hit
			print "You throw a fireball at the rabbit (-%d)" % hit
			hp -= 10
			print "Rabbit gets angry and throws a fireball at you (-10HP)" 
		else:
			print "Your life is %d" % life
			print "Rabbit life is %d" % hpRabbit
			life -= 20
			print "You hit yourself (-10HP)" 
			time.sleep(1)
			print "Rabbit takes the opportunity and hits you (-10HP)"
			
	return life, str
		
		
def die(reason):
	"""When you die"""
	if reason == "rabbit":
		time.sleep(1)
		print("Lol, a stupid rabbit killed you")
		exit(0)
	
life = 100
str = 1
start(life, str)