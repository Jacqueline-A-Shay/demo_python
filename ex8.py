# define variables
formatter = "{} {} {} {}"

# fill in the 4 {}s in formatter with 1234
print(formatter.format(1,2,3,4))
# fill in the 4{}s with 1-4 but this time in str format
print(formatter.format('one,'     'two','three','four',' .'))

# print out the T/F
print(formatter.format('True', False, False, True))

# this will print out 4 sets of {}s
print(formatter.format(formatter, formatter, formatter, formatter))

# print out 4 strings
print(formatter.format("try your", "own text", "maybe nothing","here"))
