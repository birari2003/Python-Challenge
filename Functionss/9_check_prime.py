def check_prime(n):
    if n == 1:
        print(n, "is not prime number")
    elif n > 1:
        a = False
        for i in range(2, n):
            if (n % i) == 0:
                a = True
                break
        if a == True:
            print(n, "is not prime number ")
        else:
            print(n, "is a prime number")
ck = check_prime(9)
