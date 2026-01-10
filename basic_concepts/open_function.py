'''
file = open("test.txt","w")
file.write("This is a test message \n This is the New Line")
file.close()
'''

# with block automatically close the function
with open("test.txt","w") as file:
	file.write("This is the Testing Message")
