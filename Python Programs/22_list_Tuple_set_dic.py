# Nested list, tuple, dictionary
# x = [[-----],[-----],[-----]] --> List of lists
# x = [(-----),(-----),(-----)] --> List of Tuple
# x = [{-----},{-----},{-----}] --> List of Dictionary
# x = ((-----),(-----),(-----)) --> Tuple of tuples
# x = {[-----],[-----],[-----]} --> Dictionary of list
# x = {(-----),(-----),(-----)} --> Dictionary of tuple
# x = {{-----},{-----},{-----}} --> Dictionary of Dictionary

# MUTABLE are List,set,dictionary
# IMMUTABLE are string ,number, Tuple, frozonset

# Dictionary of list
x = {'ganesh':[101, 'president',300000],
     'hari' : [102,'manager', 200000],
     'lakshmi' : [103,'Analyst',250000]}

print(x['hari'])
print(x['ganesh'][0])

# Dictionary of Dictionary
y = {'ganesh' : {'empno': 101,'job':'president','sal': 300000},
     'hari' : {'empno': 102,'job':'manager','sal': 200000},
     'lakshmi': {'empno': 103,'job':'analyst','sal': 250000}}

print(y.keys())
print(y['ganesh'])
print(y['hari']['sal'])
