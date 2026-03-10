def isPalindrom(x: int)->bool:
    if x<0:
        return False
    reverse = 0
    xcopy = x

    while x>0:
        reverse = (reverse*10)+(x%10)
        print(reverse)
        x = x//10
        print(x)
    return reverse == xcopy

result = isPalindrom(121)
print(f"{result}")
