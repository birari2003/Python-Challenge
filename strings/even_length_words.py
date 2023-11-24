a = input("Enter the string :")
a = a.split(" ")
for i in a:
    if len(i) % 2 == 0:
        print(i)
    else:
        continue
