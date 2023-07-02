# It is a collection of elements.
# Elements must enclose without {}.
# it is an unordered list & mutable object.
# list index starts with '0' and reverse index starts with '-1'.
# set does not support item indexing, item assignment and item deletion.
# The main objective of the set is it holds unique values , it eleminates duplicate values.
# It allows operations like union() (|), intersection() (&), difference() (-) and symmetric_difference() (^).

# Creating elements
a = {10, 20, 30, 40, 50, 60, 20}

# Accessing elements
print(a)
print(type(a))

#-----------------------------------------------------
# Set methods
 
# add() --> adds the element
a.add(90)
print(a)

# pop() --> delete first element 
a.pop()
print(a)

# remove() --> removes given element
a.remove(90)
print(a)

# discard() --> removes given element, if element not found it won,t show error.
a.discard(90)
print(a)

# copy() --> Returns the copy of the set.
l = {}
l = a.copy()
print(l)

# clear() --> removes all elements of list.
a.clear()
print(a)

#-----------------------------------------------------
# set operations
x = {10, 30, 40, 60}
y = {30, 60, 80, 90}

c = x|y
print(c)

c = x & y
print(c)

c = x - y
print(c)
c = y - x
print(c)

c = x^y
print(c)

#--------------------------------------------------------------
# Frozen set
# It is same as set but elements are immutable.

b = frozenset([10, 20, 30, 40 , 50])
print(b)
print(type(b))