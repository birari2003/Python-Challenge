b = int(input("Enter the turns :"))

vowel = ["a", "e", "i", "o", "u"]
li = []

for i in range(b):
    for i in range(1):
        li.clear()
        a = int(input("Enter no. of character :"))
        s = input(f"Enter the {a} character :")

        if len(s) > a:
            print("Invalid input...")
            exit()

        for i in s:
            if i not in vowel:
                li.append(i)
                
    
    print(li)
    
    if len(li) <= 4:
        print("yes")

    else:
        print("no")
    
