#Program 31. Using while loops

def create_list(size, increment):
	"""Creates a list and prints it"""
	i = 0
	numbers = []
	while i < size:
		print "New run! "
		print "At the top  i is %d" % i 
		numbers.append(i)
		
		i = i + increment
		print "Numbers now: ", numbers 
		print "At the bottom i is %d\n \n" % i 

	print "The numbers: "
	for num in numbers:
		print num

#Some testing
print "Test 1"
create_list(6, 1)
print "\n\n\nTest 2"
create_list(3, 1)
print "\n\n\nTest 3"
create_list(20,3)

#User interface
size = int(raw_input("Enter the top: "))
jump = int(raw_input("Enter the increment: "))
create_list(size, jump)
