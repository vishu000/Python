# string methods --> stringobject.methodname()
x = '---hello python---'

#-------------------------------------------------
# upper() --> Returns uppercase of string
y = x.upper()
print(y)

# lower() --> Returns lowercase of string
y = y.lower()
print(y)

# swapcase() --> Returns swaps to opposite case of string
y = x.swapcase()
print(y)

# title() --> Returns first letter to uppercase of string
y = x.title()
print(y)

# capitalize() --> Returns uppercase the first letter of string
y = x.capitalize()
print(y)

# lstrip() --> Deletes leading and trailing characters given in argument (leftside).
y = x.lstrip('-')
print(y)

# rstrip() --> Deletes leading and trailing characters given in argument (rightside).
y = x.rstrip('-')
print(y)

# strip() --> Deletes leading and trailing characters given in argument (bothsides).
y = x.strip('-')
print(y)

# ljust() --> Returns string by adding given argument till 20 characters.
y = x.ljust(20, '#')
print(y)

# rjust() --> Returns string by adding given argument till 20 characters.
y = x.rjust(20, '#')
print(y)

# startswith() --> returns True if the string starts with given argument, otherwise False
y = x.startswith('---')
print(y)

# endswith() --> returns True if the string ends with given argument, otherwise False
y = x.endswith('---')
print(y)

# count() --> counts the string.
y = x.count('o')
print(y)

# find() --> finds the first occurrence of the specified value and if value not found then returns -1.
y = x.find('p')
print(y)

# rfind() --> finds the last occurrence of the specified value and if value not found then returns -1.
y = x.rfind('m')
print(y)

# index() --> finds the first occurrence of the specified value and if value not found then gives exception error. 
y = x.index('p')
print(y)

# rindex() --> finds the last occurrence of the specified value and if value not found then gives exception error.
y = x.rindex('o')
print(y)

# replace() --> replaces a specified argument with another new specified argument.
y = x.replace('o','k')
print(y)

# split() --> splits the string into list
y = x.split()
print(y)

# rsplit() --> splits a string into a list, starting from the right.
y = x.rsplit()
print(y)

# join() --> Takes all items in an iterable and joins them into one string.
m = ("hi", "vishnu", "sai")
x = "#".join(m)
print(x)

# String validation function

# islower() --> Returns True if all characters are in lowercase, otherwise False.
y = x.islower()
print(y)

# isupper() --> Returns True if all characters are in Uppercase, otherwise False.
y = x.isupper()
print(y)

# isalpha() --> Returns True if all characters are alphabets, otherwise False.
y = x.isalpha()
print(y)

# isdigit() --> Returns True if all characters are digits, otherwise False.
y = x.isdigit()
print(y)

# isalnum() --> Returns True if all characters are both alphabets & digits, otherwise False.
y = x.isalnum()
print(y)

# istitle() --> Returns True if all words in a text start with a uppercase letter, AND the rest of the word are lower case letters, otherwise False.
y = x.istitle()
print(y)

# isspace() --> Returns True if all the characters in a string are whitespaces, otherwise False.
y = x.isspace()
print(y)