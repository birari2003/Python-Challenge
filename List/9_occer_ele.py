def occerence_of_element(li, x):
    count = 0
    for i in li:
        if i == x:
            count += 1
    print(count)

c = occerence_of_element([10,12,15,10,18,19], 10)
