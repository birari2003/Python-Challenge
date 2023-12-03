def count_even_odd(li):
    count1 = 0
    count2 = 0
    for i in li:
        if i %2 == 0:
            count1 += 1
        else:
            count2 += 1
    print(f"Total count of even numbers is {count1} and odd is {count2}")

A = count_even_odd([2,1,3,5,6,-8,0,5,11])