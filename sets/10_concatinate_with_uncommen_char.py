s1 = "abcs"
s2 = "cxzca"

for i in s1:
    if i in s2:
        s1 = s1.replace(i, "")
        s2 = s2.replace(i, "")

print(s1 + s2)
