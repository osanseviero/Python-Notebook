# Program 20. Files and functions 
# Use text20.txt

from sys import argv
script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)	#Sends us back to byte 0
	
def print_a_line(line_count, f):
	print line_count, f.readline()	#It will jump a line


current_file = open(input_file)				#Opening
print "First let's print the file: \n"
print_all(current_file)						#Printing

print "Now we'll rewind \n"
rewind(current_file)

#Printing line by line
print "Now let's print some lines"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line += 1	
print_a_line(current_line, current_file)
