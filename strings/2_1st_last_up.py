a = input("Enter the string :")
b = []
for i in range(len(a)):
    if a[1:] == i and a[:-1] == i:
        a.capitalize()
        b.append(i)
        print(b)
    