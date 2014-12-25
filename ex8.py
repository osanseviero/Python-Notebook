#Program 8. Using strings and variables

#Variable that receives 4 elements (look the difference between %s and %r)
formatter = "%r %r %r %r"
# formatter = "%s %s %s %s


print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (		#Several lines string
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)