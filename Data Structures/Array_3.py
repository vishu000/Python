m = int(input("size of the list : "))

l =[]
for i in range(1,m+1):
    if i%2 == 1:
        l.append(i)
print(l)
