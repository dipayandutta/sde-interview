people = [
		{"name": "Alice","age":30},
		{"name": "Bob","age":23},
		{"name": "Charlie","age":33}
]

# Now to srote the list of the people based on the age

sorted_people = sorted(people,key=lambda person: person["age"])
print(sorted_people)
