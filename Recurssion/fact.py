def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)

result= factorial(5)
print(result)
