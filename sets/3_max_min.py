# def maximum(s):
#     print(max(s))
#     print(min(s))


    

# M = maximum({1,2,3,4,5,6})

        
# cook your dish here
a = int(input("Enter no. of character :"))
vowel = ["a", "e", "i", "o", "u"]
li = []
for i in range(1):
    s = input(f"Enter the {a} character :")

    if len(s) > a:
        print("Invalid input...")
        exit()

    for i in s:
        if i not in vowel:
            li.append(i)
   
if len(li) < 4:
    print("yes")

else:
    print("no")
    
