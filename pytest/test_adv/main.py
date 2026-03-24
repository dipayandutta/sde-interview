def get_even_numbers(numbers):
    even_number = []
    for number in numbers:
        if number%2 == 0:
            even_number.append(number)

    return even_number

def multiply(a,b):
    return a*b 

def divide(a,b):
    if b<=0:
        raise ValueError("Cannot Divied By Zero")
    
    else:
        return a/b 