#Program 10. Escape sequence and printing.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print ("Hello: \n\t Backspace kills stuff. \b \a\b\b\b\b\nMy name is osan")
print ("\tThere are different ways \v of doing stuff")
print ("\tFor example \\f does \f stuff")
print ("\tWho knows what I'm \rdoing") #The \r takes it to the start