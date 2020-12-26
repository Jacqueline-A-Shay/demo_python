#I "understand" joe

#"I am 6'2\" tall." # escape double quote inside string
#'I am 6\'2" tall.' # escape single quote inside string

tabby_cat = "\tI'm tabbed in."

persian_cat = "I'm split\non a line"

backslash_cat = "I'm\\ a \\ cat."

fat_cat = """
I'll do a list:
\t&^ Cat food
\t* fishies
\t* catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# \\
# \' \"
# \a  ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n new line ASCII linefeed

#\N{name} Character named name in the unicode database (unicode only)

# \r carriage return
var2 = 'cajodiafj\r12345678'
print(var2)

var =" \a"
print(var) 

singles = '''
test " multi" lines
test test
'''
print(singles)
