#Program 17. Copying files
#Run it with original17.txt and tocopy17.txt

from sys import argv
from os.path import exists	#We import a command that will return True the file exists.

script, from_file, to_file = argv

#Before
	# in_file = open(from_file, 'r')	#We open the file in read mode
	# indata = in_file.read()			#We read it

#We combine the last two steps
indata = open(from_file, 'r').read()

	#print "The input file is %d bytes long" % len(indata)		#We tell how many bytes there are in the file
	#print "Does the output file exist? %r" % exists(to_file)	#exists(to_file) will return True if it exists and False if it does not
	
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input("?")

	#out_file = open(to_file, 'w')			#We open the to_copy file in write mode
	#out_file.write(indata)					#We write indata (all the info read in the original file)

#We combine the last two steps
open(to_file, 'w').write(indata)

print "Alright, all done"

