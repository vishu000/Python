l1 = [2200, 2350, 2600, 2130, 2190]
extra_spent = l1[1] - l1[0]
print(extra_spent) 
first_quarter = l1[0] + l1[1] + l1[2] 
print(first_quarter)

for i in range(len(l1)):
    if l1[i] == 2000:
        print("spent exactly 2000")
        break
    else:
        print("Noo")
        break
l1.append(1980)
print(l1)

l1[3] = l1[3] - 200
print(l1)