name: str ='Bob'
age: int = 30

template = t'Hello, {name}! You are {age} years old!'
print(template.strings)
print(template.interpolations)
print(template.values)
