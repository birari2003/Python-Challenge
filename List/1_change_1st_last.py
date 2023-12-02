li = [1, 2, 3, 5, 6, 8, 9]
a = li[0]
li[0] = li[-1]
li[-1] = a
print(li)