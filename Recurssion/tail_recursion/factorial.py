'''
find the factorial of a number using
tail recursion
'''

def tail_recursion_factorial(n,result=1):
    if n == 0:
        return result 
    return tail_recursion_factorial(n-1, n * result)

print(tail_recursion_factorial(5))
