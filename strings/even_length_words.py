a = input("Enter the string :")
a = a.split(" ")
b = []
for i in a:
    if len(i) % 2 == 0:
        b.append(i)
    else:
        continue
print(b)

