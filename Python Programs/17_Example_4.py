# Accept the string and count total number vowels.
x = input("Enter the string : ")
cnt = 0
for i in x:
    if i in "aeiouAEIOU" :
        cnt += 1
print("total number of vowels : ",cnt)