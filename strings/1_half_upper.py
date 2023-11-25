test = "geeksforgeeks"

print("The original string is : " + str(test))

hlf_idx = len(test) / 2

res = ""
for idx in range(len(test)):
    if idx >= hlf_idx:
        res += test[idx].upper()
    else:
        res += test[idx]

print("The resultant string : " + str(res))

