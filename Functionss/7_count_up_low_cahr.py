def check_upper_lower(st):
    count1 = 0
    count2 = 0
    for i in st:
        if i.isupper():
            count1 += 1
        elif i.islower():
            count2 += 1

    print("The no. of upper case letters are :", count1)
    print("The no. of upper case letters are :", count2)


ck = check_upper_lower("The quick Brow Fox")
