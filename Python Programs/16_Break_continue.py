# break (print values from 1 to 4)
i = 1
while i <= 10:
  if i == 5:
    break
  print(i)
  i += 1

#------------------------------------------------------------
# continue (print values from 1 to 10 except 5)
j = 1
while j <= 10:
  if j == 5:
    j += 1
    continue
  print(j)
  j += 1