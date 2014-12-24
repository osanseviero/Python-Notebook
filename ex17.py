#Program 17. Copying files
from sys import argv
from os.path import exists	#We import a command that will return True the file exists.

script, from_file, to_file = argv

#Before
	# in_file = open(from_file, 'r')
	# indata = in_file.read()

indata = open(from_file, 'r').read()

	#print "The input file is %d bytes long" % len(indata)

	#print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input("?")

	#out_file = open(to_file, 'w')
	#out_file.write(indata)
open(to_file, 'w').write(indata)

print "Alright, all done"

