# It is a group of key pair values.
# The elements must enclose within {} and mutable object.
# The keys must be unique and gives good performance over list.

# creating a dictionary
d1 = {'ap' : 'hyd' , 'tn' : 'chennai', 'kn': 'bangalore'}
d2 = {'unix' : '3000','python' : '5000','aws' : '9000'}

# Accessing keypair values
print(d1)
print(type(d1))

# Adding key pairs
d1['up'] = 'lucknow'
d2['sql'] = '3000'
print(d1)
print(d2)

# Modifying key pairs
d1['ap'] = 'amaravathi'
d2['unix'] = '5000'
print(d1)
print(d2)

# Deleteing key pairs
del d1['tn']
del d2['aws']
del d2
print(d1)
#print(d2) # Name error

# Dictionary methods
# keys()---> Returns only keys
u = d1.keys()
print("keys :",u)

# values()---> Returns only values
u = d1.values()
print("values :",u)

# items()---> Returns only keys and values
u = d1.items()
print(u)

# get()---> Returns only key value if not found no error.
u = d1.get('up')
print(u)
v = d1.get('tn')
print(v)

# pop()---> Returns and delets given key pair value 
u = d1.pop('kn')
print(u)
print(d1)

# popitem() ---> Returns and deletes last key pair.
u = d1.popitem()
print(u)
print(d1)

# update()---> To append a dictionary
a = {1 : 10, 2 : 20}
a.update(d1)
print(a)

# copy()---> To copy a dictionary
u = a.copy()
print(u)

# clear()---> To return all key pairs
d1.clear()
print(d1)
