li = [1,2,3,4,5,6,7,8,9]
a, b = map(int, input("enter the two values :"))
c = li[a]
li[a] = li[b]
li[b] = c
print(li)