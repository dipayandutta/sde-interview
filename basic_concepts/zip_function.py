names = ["Alice","Bod","Charlie","David"]
ages = [30,25,35,20]

# with out the zip() function
for idx in range(min(len(names), len(ages))):
	name = names[idx]
	age = ages[idx]
	print(f"{name} is {age} years old")

print("----------------------")
print("Using the zip() function()")
# Using the zip() function
combined = list(zip(names,ages))
print(combined)

for name, age in combined:
	print(f"{name} is {age} years old")
