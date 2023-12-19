def check_palindrome_str(st):
    if st == st[::-1]:
        print(st, "is palindrome")
    else:
        print(st, "is not palindrome")
  
ck = check_palindrome_str("nurses run")

