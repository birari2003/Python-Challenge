def return_distinct_ele(li):
    L = []
    for i in li:
        if i not in L:
            L.append(i)
    print(L)

R = return_distinct_ele([1,2,3,3,3,3,4,5])