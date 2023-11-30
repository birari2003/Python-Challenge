a = input("Enter the string :")
c = ""
for i in a:
    if i not in c:
        c += i
    else:
        continue
print(c)
