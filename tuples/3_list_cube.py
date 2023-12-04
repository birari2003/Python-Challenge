def list_of_cube_tuple(li):
    t = list(map(lambda x: (x, x**3), li))
    print(t)

T = list_of_cube_tuple([1,2,3,4])


