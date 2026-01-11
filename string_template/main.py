from string import Template

template = Template('Hello, $name! You are $age years old')
message = template.substitute(name='Bob',age=50)

print(message)
