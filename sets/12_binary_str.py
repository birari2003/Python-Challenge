str = "10101000101"
count = 0
t = "01"
for i in str:
    if i not in t:
        count = 1
        break
    else:
        pass

if count == 1:
    print("no")
else:
    print("yes")