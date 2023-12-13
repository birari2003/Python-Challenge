li1 = [1,2,3,4,5,6]
li2 = [4,5,6,7,8]

L1 = []
L2 = []

for i in li1:
    if i not in li2:
        L1.append(i)

for j in li2:
    if j not in li1:
        L2.append(j)

print(f"missing value in list 1 is {L2}")
print(f"additional value in list 2 is {L1}")
print(f"missing value in list 2 is {L1}")
print(f"additional value in list 1 is {L2}")