# + - / * % < > <= >=

# print out a string, the sentence
print("I will now count my chickens")

# originally, thought it will do the math and print out the strings
# string = str = the sentence, English part
# but....I forgot about everything in the " " would be treated as str...... 
# so I made my solution in the following print statement
# the 3 sets of " " allowed me to print multiple lines and save some typing (of print statement)
print("""Hens 25+30/6
roosters 100 - 25 * 3 % 4,
now i will count the eggs:
3+2+1- 5 +4 % 2 -1/4+6,
'is it true that 3+2<5-7?',
3+2<5-7,
'what is 3+2? ', 3+2,
'what is 5-7? ', 5-7,
'oh! that why it's False'
""")

# so this is the real print str plus doing math all together
# again, triple " " allowed me to print across multiple lines
# a set of {} allow me to refer the math result specified location e.g. 5+15 goes after got and before cow
# :.2f means only present 2 decimal points of a float
# .format allow me to specify the math relative locations
print("""we've got {} cow 
and {:.2f}"""
.format(5+15, 13%2))
