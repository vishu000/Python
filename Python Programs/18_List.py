# it is a collection of homogenous or hetrogenous elements.
# Elements must enclose within [] and mutable object.
# list index starts with '0' and reverse index starts with '-1'.

a = [10, 20, 30, 40, 50, 60]
print(a)
print(type(a))
print(a[2])
print(a[-3 : ])
print(a[ : : 2])
print(a[ : : -1])

# modifying elements
a[2] = 300
print(a)

# Deleting elements
del a[2]
print(a)
del a[:]
print(a)

# List cancatenation
x = [10, 20, 30, 40, 50]
y = [10, 20, 30, 40, 50]
print(x + y)
z = []
for i in x:
    z.append(i + 5)
print(z)

# List Multiplication
print(x*3)
r = []
for i in y:
    r.append(i * 5)
print(r)

# List function
H = [100, 600, 200, 500, 300, 900]
print(len(H))
print(max(H))
print(min(H))
print(sum(H))
print(sorted(H))
H.reverse()
print(H)

# enumerate() --> Returns index and value.
for i, j in enumerate(H):
    print(i + 1 ,":", j )

# LIst methods

# append(element) --> adds element.
B = [10, 20, 30]
B.append(40)
print(B)

# extent([ele1, ele2, .......]) --> adds elements.
C = [30, 60]
B.extend(C)
print(B)

# insert(position, element) --> inserts elements.
B.insert(2, 90)
print(B)

# pop(index) --> removes element of specified index.
B.pop(0)
print(B)

# remove(element) --> removes specified element.
B.remove(20)
print(B)

# count(element) --> Counts the specified element appears in the list.
u = B.count(30)
print(u)

# index(element) --> Returns the index of specified element.
u = B.index(60)
print(u)

# reverse() --> reverses the list.
B.reverse()
print(B)

# sort() --> sorts the list.
B.sort()
print(B)

# copy() --> Returns the copy of the list.
l = []
l = B.copy()
print(l)

# clear() --> removes all elements of list.
B.clear()
print(B)