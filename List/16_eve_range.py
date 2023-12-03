a = int(input("enter start :"))
b = int(input("Enter last :"))
li = []
for i in range(a, b+1):
    if i % 2 == 0:
        li.append(i)
print(li)