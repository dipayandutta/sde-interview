'''
You have a list of numbers and want to square to each one.
'''

numbers = [1,2,3,4,5]
squares = map(lambda x: x *x , numbers)
print(squares)
print(list(squares))
