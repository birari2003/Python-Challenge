a = input("Enter a string :")
b = input("Enter character to remove :")


for i in a:
    if i == b:
        continue
    print(str(i))