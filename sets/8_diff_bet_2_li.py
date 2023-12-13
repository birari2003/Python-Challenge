l1 = [10, 15, 20, 25, 30, 35, 40]
l2 = [25, 40, 35]

L = []
for i in l1:
    if i in l2:
        continue
    else:
        L.append(i)
print(L)


