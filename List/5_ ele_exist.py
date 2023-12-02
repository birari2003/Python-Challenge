def ele_in_list(list, element):
    if element in list:
        return True
    else:
        return False

e = ele_in_list([1,2,3,4,6,7], 9)
print(e)