def reversed_str(st):
    a = ""
    for i in st[::-1]:
        a += i
    print(a)

s = reversed_str("1234abcd")