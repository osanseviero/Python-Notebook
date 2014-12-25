#Program 21. Using returns


def add(a,b):
	#print "%d + %d" % (a,b)
	return a + b

def substract(a,b):
	#print "%d - %d" % (a,b)
	return a - b

def multiply(a,b):
	#print "%d * %d" % (a,b)
	return a * b

def divide(a,b):
	#print "%d / %d" % (a,b,)
	return a / b

age = add(10, 8)
height = substract(190,10)
weight = multiply(20,30)
iq = divide(200,2)

print "Age %d\nHeight: %d\nWeight: %d\nIQ: %d" % (age, height, weight, iq)

print "A puzzle"
what = add(age, substract(height, multiply(weight, divide(iq,2))))
print "That becomes ", what