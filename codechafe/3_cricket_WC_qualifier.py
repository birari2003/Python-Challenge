a = int(input())

for i in range(a):
    x, y = map(int, input().split())
    if (x * y) % 2 == 0:
        print("yes")
    else:
        print("no")
