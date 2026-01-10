tasks = ["Prepare python","Revised Linux","Learn Basic of Go"]

for index in range(len(tasks)):
	task = tasks[index]
	print(f"{index+1} --> {task}")

for index,task in enumerate(tasks):
	print(f"{index+1}--> {task}")
