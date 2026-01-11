from string.templatelib import Template

def built_template(t_string: Template) -> str:
	values: list[str] = []
	
	for i in t_string:
		if isinstance(i,str):
			values.append(i)
		else:
			values.append(i.value)

	return ''.join(values)

name:	str = 'Bob'
profession:	str = 'Chef'
template:	Template = t'Your name is {name} and your profession is {profession}'

print(template)
print(built_template(template))
