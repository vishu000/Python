# List comprehension :
#     --> List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#     --> newlist = [expression for item in iterable if condition == True]

f1 = [1, 2, 3, 4, 5]
newlist = [i for i in f1 if i < 5]
print(newlist)

# Dictionary comprehension :
#     --> Dictionary comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#     --> newDictionary = {expression for item in iterable if condition == True}

input = [1,2,3,4,5,6,7]
dict = {var:var ** 2 for var in input if var % 2 != 0}
print(dict)

# Set comprehension :
#     --> Set comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#     --> newset = {expression for item in iterable if condition == True}

input = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
set = {var for var in input if var % 2 == 0}
print(set)

# Generator comprehension :
#     --> Set comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#     --> Generator Comprehensions are very similar to list comprehensions.
#     --> One difference between them is that generator comprehensions use circular brackets whereas list comprehensions use square brackets.
#     --> generators don’t allocate memory for the whole list. Instead, they generate each value one by one which is why they are memory efficient.
#     --> newlist = [expression for item in iterable if condition == True]

input = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
gen = (var for var in input if var % 2 == 0)
for var in gen:
    print(var, end = ' ')

