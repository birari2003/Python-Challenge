def even_ele(li):
    L = []
    for i in li:
        if i % 2 == 0:
            L.append(i)
    print(L)

E = even_ele([1,2,3,4,5,6,7,8])