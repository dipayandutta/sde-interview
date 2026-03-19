def tail_recursion(n):
    if n==0:
        return n
    print(n)
    tail_recursion(n-1)
tail_recursion(5)
