def reverse(x: int)-> int:
    sign = -1 if x<0 else 1
    x = abs(x)
    reverse = 0
    while x>0:
        reverse = (reverse*10)+(x%10)
        x = x//10
    return sign*reverse

result=reverse(-123)
print(f"Result is {result}")
