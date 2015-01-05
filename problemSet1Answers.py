# Problem set 1.

# Exercise 1: Reverse a string
def reverse_string(string):
	reversed = string[::-1]	#We start at the end and keep going until the beginning
	return reversed
print reverse_string("hey")


# Exercise 2: Factorial
def FirstFactorial(num):
	factorial = 1
	if num >0:
		factorial = FirstFactorial(num - 1) * num	#We'll see more of this later. There are other ways to solve the problem
	return factorial
a = FirstFactorial(4)
print a

# Exercise 3: Longest word in string
def LongestWord(sen):
	for char in sen:
		if not char.isalnum():
			sen = sen.replace(char, ' ') #First step will be to ignore punctuation
	as_list = sen.split(' ')
	a = as_list[0]
	for element in as_list:
		if len(element) > len(a):
			a = element
	return a
print LongestWord("how are you doing today, sir?")
	
# Exercise 4: Adding
# Have the function SimpleAdding(num) add up all the numbers from 1 to num. 
def SimpleAdding(num):	#Try doing this like in exercise 2 ;)
	a = 0
	while num > 0:
		a = a + num
		num -= 1
	return a
print SimpleAdding(5)
	
	
	
	