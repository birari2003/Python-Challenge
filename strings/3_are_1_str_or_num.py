j = input("Enter a string :")

ans = "no"

for i in j:
    if i.isdigit():
        ans = "yes"
        break
print(ans)
