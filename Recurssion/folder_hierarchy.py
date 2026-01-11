import os

def folder_contents(path):
	for item in os.listdir(path):
		item_path = os.path.join(path,item)
		if os.path.isfile(item_path):
			print(f"Found a File: {item_path}")
		elif os.path.isdir(item_path):
			print(f"Entering folder: {item_path}")
			folder_contents(item_path)
folder_contents("/Users/dipayandutta/Developer/python/sde-interview/")
