strings = ["python","RedHat","Go","kubernetes"]

def longer_than_4(string):
	return len(string)>4

filtered = filter(longer_than_4,strings)
print(list(filtered))
