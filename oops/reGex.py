#regular expressions
# import re
# value="this  is a string" 
# output=re.search("^This.*string$", value)
# print(output)
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"
# This looks like a regular expression that is used to check if a string meets certain criteria.
# The regular expression is made up of several "lookaheads",
# which are special types of assertions that check for the presence of certain patterns in the string without consuming any characters.
# The first lookahead ((?=.*[a-z])) checks if the string contains at least one lowercase letter.
# The second lookahead ((?=.*[A-Z])) checks if the string contains at least one uppercase letter.
# The third lookahead ((?=.*[!@#$%^&*()_+=-])) checks if the string contains at least one of the special characters listed inside the square brackets. 
# The fourth lookahead ((?=.{8,})) checks if the string is at least 8 characters long.
# Together, these lookaheads ensure that the string contains at least one lowercase letter, one uppercase letter, one special character, and is at least 8 characters long.
#raw string

# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrences	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"
# |	Either or	"falls|stays"	
# ()	Capture and group