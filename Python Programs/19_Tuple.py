# it is a collection of homogenous or hetrogenous elements but imutable.
# Elements must enclose within () and mutable object.
# list index starts with '0' and reverse index starts with '-1'.
# Tuple gives good performance over list.

a = (10, 20, 30, 40, 50, 30)

# Accessing elements
print(a)
print(type(a))
print(a[2])
print(a[-3 : ])
print(a[ : : 2])
print(a[ : : -1])

# enumerate() --> Returns index and value.
for i, j in enumerate(a):
    print(i + 1 ,":", j )

# count(element) --> Counts the specified element appears in the list.
u = a.count(30)
print(u)

# index(element) --> Returns the index of specified element.
u = a.index(50)
print(u)
