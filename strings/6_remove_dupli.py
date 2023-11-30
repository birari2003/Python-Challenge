a = input("Enter the string :")
b = a.split()
print(b)
c = ""
for i in b:
    if i not in c:
        c += i
    else:
        continue

print(c)
