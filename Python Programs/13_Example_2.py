import random 

x = random.randint(1, 10)
n = int(input("take a guess between [1 - 10] : "))

if n == x:
    print("your guess is correct")
else:
    print("your guess is incorrect")