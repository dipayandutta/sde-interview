'''
find a factorial of a number using 
Head Recursion
'''

def head_recursion_factorial(n):
    if n == 1:
        return 1 
    result = head_recursion_factorial(n-1)
    return n * result 

print(head_recursion_factorial(5))
